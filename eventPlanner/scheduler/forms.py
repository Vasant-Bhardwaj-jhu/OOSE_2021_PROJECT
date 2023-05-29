from django import forms
from .support import states

choices = [
    (1, "Strongly Dislike"),
    (2, "Somewhat Dislike"),
    (3, "Neutral"),
    (4, "Somewhat Like"),
    (5, "Strongly Like")
]

category_choices = [
    ("music", "Music"),
    ("visual-arts", "Visual"),
    ("performing-arts", "Performing Arts"),
    ("film", "Film"),
    ("lectures-books", "Lectures"),
    ("fashion", "Fashion"),
    ("food-and-drink", "Food"),
    ("festival-fairs", "Festivals"),
    ("charities", "Charity"),
    ("sports-active-life", "Sports"),
    ("nightlife", "Nightlife"),
    ("kids-family", "Family"),
    ("all", "No filter")
]

time_zones = [
    (-5, "eastern standard time"),
    (-6, "central time"),
    (-7, "mountain time"),
    (-8, "pacific standard time"),
]

cost_choices = [
    (20, "$"),
    (100, "$$"),
    (1000000, "$$$")
]


class PreferenceForm(forms.Form):
    music = forms.IntegerField(label="Music:", required=True, initial=3, widget=forms.Select(choices=choices))
    visual = forms.IntegerField(label="Visual:", required=True, initial=3, widget=forms.Select(choices=choices))
    performing = forms.IntegerField(label="Performing:", required=True, initial=3, widget=forms.Select(choices=choices))
    film = forms.IntegerField(label="Film:", required=True, initial=3, widget=forms.Select(choices=choices))
    lectures = forms.IntegerField(label="Lectures", required=True, initial=3, widget=forms.Select(choices=choices))
    fashion = forms.IntegerField(label="Fashion", required=True, initial=3, widget=forms.Select(choices=choices))
    food = forms.IntegerField(label="Food", required=True, initial=3, widget=forms.Select(choices=choices))
    festivals = forms.IntegerField(label="Festivals", required=True, initial=3, widget=forms.Select(choices=choices))
    charity = forms.IntegerField(label="Charity", required=True, initial=3, widget=forms.Select(choices=choices))
    sports = forms.IntegerField(label="Sports", required=True, initial=3, widget=forms.Select(choices=choices))
    nightlife = forms.IntegerField(label="Night Life", required=True, initial=3, widget=forms.Select(choices=choices))
    family = forms.IntegerField(label="Family", required=True, initial=3, widget=forms.Select(choices=choices))


class EventSearchForm(forms.Form):
    start_time = forms.DateTimeField(label="Free From:", required=True, widget=forms.DateTimeInput(attrs={
        "type": "datetime-local"
    }))
    end_time = forms.DateTimeField(label="Free Until:", required=True, widget=forms.DateTimeInput(attrs={
        "type": "datetime-local"
    }))
    address1 = forms.CharField(label="Street Address:", max_length=200, required=True)
    city = forms.CharField(label="City:", max_length=200, required=True)
    state = forms.CharField(label="State:", required=True,
                            widget=forms.Select(choices=states.get_all_states_reversed().items()))
    country = forms.CharField(label="Country:", max_length=200, required=True)
    optimized = forms.BooleanField(label="Optimize Schedule (You might need to wait a few minutes)", required=False)
    start_day = forms.TimeField(label="day starts at:", required=True,
                                widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}))
    end_day = forms.TimeField(label="day ends at:", required=True,
                              widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}))
    time_zone = forms.CharField(label="What time zone?: ", required=True,
                                widget=forms.Select(choices=time_zones))


class EventFilterForm(forms.Form):
    category = forms.CharField(label="Category", initial="all", widget=forms.Select(choices=category_choices))
    cost = forms.FloatField(label="Cost", widget=forms.Select(choices=cost_choices))
