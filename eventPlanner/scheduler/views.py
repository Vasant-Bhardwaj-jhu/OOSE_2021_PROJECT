from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import PreferenceForm, EventSearchForm, EventFilterForm
from .models import User, Event
from .support import states, algorithm, event_finder
import datetime
from dateutil import parser
import pytz


def user_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if 'events' not in request.session:
        request.session['events'] = []

    return render(request, "scheduler/profile.html", context={
        "user": request.user,
        "navItems": {
            "Profile": reverse("profile"),
            "Logout": reverse("logout"),
        }
    })


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        current_user = authenticate(request, username=username, password=password)
        if current_user:
            login(request, current_user)
            # Event.objects.all().delete()
            # Event.objects.values('temporary', False).delete()
            Event.objects.all().delete()
            for state in states.get_all_states().values():
                event_finder_object = event_finder.EventFinder(
                    location=state,
                    start_time=int(parser.parse(datetime.datetime.now().isoformat()).timestamp())
                )
                # print("we running")
                event_finder_object.save_all_events()
            return HttpResponseRedirect(reverse("user"))
        else:
            messages.error(request, message="Invalid Username and/or Password")
            return render(request, "scheduler/login.html")
    return render(request, "scheduler/login.html")


@login_required(login_url='login')
def profile_view(request):
    return render(request, "scheduler/profile.html", context={
        "navItems": {
            "Profile": reverse("profile"),
            "Logout": reverse("logout"),
        }
    })


def logout_view(request):
    logout(request)
    messages.success(request, message="Successfully Logged Out")
    return render(request, "scheduler/login.html")


def register_view(request):
    if request.method != "POST":
        return render(request, "scheduler/register.html")
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    username = request.POST["username"]
    password = request.POST["password"]
    confirm_password = request.POST["confirm_password"]
    address1 = request.POST["address1"]
    city = request.POST["city"]
    state = states.get_state_code(request.POST["state"])
    country = request.POST["country"]

    if state is None:
        messages.error(request, message="Invalid State")
        return render(request, "scheduler/register.html")

    if password != confirm_password:
        messages.error(request, message="Passwords do not Match")
        return render(request, "scheduler/register.html")

    try:
        current_user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
            address1=address1,
            city=city,
            state=state,
            country=country,
        )
        current_user.save()
        login(request, current_user)
    except IntegrityError:
        messages.error(request, "Email address already in use")
        return render(request, "scheduler/register.html")
    messages.success(request, "Successfully Created User")
    # return HttpResponseRedirect(reverse('preferences'))
    return render(request, "scheduler/preferences.html")


@login_required(login_url='login')
def preferences_view(request):
    print(request.method)
    if request.method != "POST":
        print("GET preferences view")
        return render(request, "scheduler/update_preferences.html")
    print("POST preferences view")
    # GET on bottom
    music = request.POST["music"]
    visual = request.POST["visual"]
    performing = request.POST["performing"]
    film = request.POST["film"]
    lectures = request.POST["lectures"]
    fashion = request.POST["fashion"]
    food = request.POST["food"]
    festivals = request.POST["festivals"]
    charity = request.POST["charity"]
    sports = request.POST["sports"]
    nightlife = request.POST["nightlife"]
    family = request.POST["family"]
    print(music)

    try:
        current_user = User.objects.get(pk=request.user.pk)
        print(current_user)
        current_user.music = music
        current_user.visual = visual
        current_user.performing = performing
        current_user.film = film
        current_user.lectures = lectures
        current_user.fashion = fashion
        current_user.food = food
        current_user.festivals = festivals
        current_user.charity = charity
        current_user.sports = sports
        current_user.nightlife = nightlife
        current_user.family = family
        current_user.save()
    except IntegrityError:
        messages.error(request, message="Invalid Selection")
        if request.POST.get('name') == 'preference-form':
            return render(request, "scheduler/preferences.html", context={
                # "preference_form": PreferenceForm(),
                "navItems": {
                    "Profile": reverse("profile"),
                    "Logout": reverse("logout"),
                }
            })
        else:
            return render(request, "scheduler/preferences.html", context={
                # "preference_form": PreferenceForm(),
                "navItems": {
                    "Profile": reverse("profile"),
                    "Logout": reverse("logout"),
                }
            })
    print(request.POST)
    if request.POST["registration"] == 'registration':
        print("should reverse login")
        return HttpResponseRedirect(reverse('login'))
    else:
        print("should reverse profile")
        return HttpResponseRedirect(reverse('profile'))

    return render(request, "scheduler/preferences.html", context={
        # "preference_form": PreferenceForm(),
        "navItems": {
            "Profile": reverse("profile"),
            "Logout": reverse("logout"),
        }
    })

@login_required(login_url='login')
def search_view(request):
    if request.method != "POST":
        return render(request, "scheduler/search2.html")
    print(request.POST)
    start_time = request.POST["start_time"]
    start_time = parser.parse(start_time)
    print(start_time)
    end_time = request.POST["end_time"]
    end_time = parser.parse(end_time)
    print(end_time)
    address1 = request.POST["address1"]
    print(address1)
    city = request.POST["city"]
    print(city)
    state = request.POST["state"]
    print(state)
    day_start = request.POST["start_day"]
    print(day_start)
    day_end = request.POST["end_day"]
    print(day_end)
    time_zone = int(request.POST["time_zone"])
    print(time_zone)
    optimized = request.POST["schedule"]
    print(optimized)
    schedule_window = (end_time - start_time).days
    if optimized and schedule_window > 31:
        messages.error(request, message="Cannot create schedule with time greater than one month")
        return render(request, "scheduler/search2.html", context={
            "event_search_form": EventSearchForm(),
        })

    if state is None:
        messages.error(request, message="Invalid State")
        return render(request, "scheduler/search2.html", context={
            "event_search_form": EventSearchForm(),
        })

    request.session['events'] = []

    events = Event.objects.filter(
            start_time__gte=start_time,
            end_time__lte=end_time,
            city=city,
            state=state,
    )
    if optimized:
        events = algorithm.get_temp_schedule(address1, events, request.user)
    else:
        events = algorithm.sort_events_by_time(events)
        print(events)
        # daily_schedules.append(())

    for event in events:
        event.start_time_display = event.start_time + datetime.timedelta(hours=time_zone)
        event.end_time_display = event.end_time + datetime.timedelta(hours=time_zone)
        print("Name" + event.name + ", visual time: " + str(event.start_time_display.hour) + ", actual time: " + str(event.start_time.hour))
        event.save()
        request.session["events"] += [event.pk]
    return HttpResponseRedirect(reverse('events'))


def create_blocks(start_time, end_time, day_start, day_end, schedule_window):
    daily_schedules = []
    # start_year = start_time.year
    # print("start time.years ok")
    utc = pytz.UTC
    day_start_dt = utc.localize(
        datetime.datetime(start_time.year, start_time.month, start_time.day, day_start.hour, day_start.minute,
                          day_start.second))
    day_end_dt = utc.localize(
        datetime.datetime(start_time.year, start_time.month, start_time.day, day_end.hour, day_end.minute,
                          day_end.second))
    delt = datetime.timedelta(days=1)
    if schedule_window == 0:
        daily_schedules.append((start_time, end_time))
    else:
        if start_time < day_end_dt:
            daily_schedules.append((start_time, day_end_dt))

        start = start_time.day  # start day
        end = end_time.day  # end day
        for i in range(schedule_window - 1):
            daily_schedules.append((day_start_dt, day_end_dt))
            day_start_dt += delt
            day_end_dt += delt

        if end_time > day_end_dt:
            daily_schedules.append((day_start_dt, end_time))

    return daily_schedules


@login_required(login_url='login')
def events_view(request):
    event_pks = request.session['events']
    events = [Event.objects.get(pk=event_pk) for event_pk in event_pks]

    if request.method == "POST":
        event_filter_form = EventFilterForm(request.POST)
        filtered_events = []
        if event_filter_form.is_valid():
            category = event_filter_form.cleaned_data["category"]
            cost = event_filter_form.cleaned_data["cost"]
            for event in events:
                if event.cost <= cost:
                    if category != "all":
                        if event.category == category:
                            filtered_events.append(event)
                    else:
                        filtered_events.append(event)
            events = filtered_events
    return render(request, "scheduler/events.html", context={
        "events": events,
        "navItems": {
            "Profile": reverse("profile"),
            "Logout": reverse("logout"),
        },
        "event_filter_form": EventFilterForm(),
    })
