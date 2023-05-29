from datetime import datetime
# import places
from . import travel


class TravelTimeMatrix:
    def __init__(self, origin, events):
        self.num_map = {}
        for index, value in enumerate(events):
            self.num_map[value] = index

        self.origin = origin
        self.events = events
        self.time_array = self.compute_distance()

    def compute_distance(self):
        event_list = self.events
        q = len(event_list)
        w = q + 1
        distance = [[0 for _ in range(w)] for _ in range(w)]
        for i in range(q):
            current_travel_time = travel.get_travel_time(self.origin, event_list[i].address1)
            distance[0][i] = distance[i][0] = current_travel_time
        for i in range(1, q):
            for j in range(i + 1, q):
                current_travel_time = travel.get_travel_time(
                    event_list[i].address1,
                    event_list[j].address1,
                )
                distance[i][j] = distance[j][i] = current_travel_time
        return distance

    def get_time(self, event1, event2):
        row = self.num_map[event1]
        col = self.num_map[event2]
        return self.time_array[row][col]


def check_conflict(event1, event2, time_matrix):
    travel_time = time_matrix.get_time(event1, event2)
    if travel_time == 0:
        return (
            event1.end_time >= event2.start_time
            and event2.end_time >= event1.start_time
        )
    else:
        return (
            event1.end_time + travel_time >= event2.start_time
            and event2.end_time + travel_time >= event1.start_time
        )


def closest_non_conflict_event(time_matrix, event_index):
    current_index = event_index - 1
    event_list = time_matrix.events
    e = event_list[event_index]
    while current_index >= 0:
        current_event = event_list[current_index]
        if not check_conflict(current_event, e, time_matrix):
            return current_event
        current_index -= 1
    return None


def closest_non_conflict_index(time_matrix, event_index):
    if event_index >= len(time_matrix.events):
        return -1
    current_index = event_index - 1
    event_list = time_matrix.events
    e = event_list[event_index]
    while current_index >= 0:
        current_event = event_list[current_index]
        if not check_conflict(current_event, e, time_matrix):
            return current_index
        current_index -= 1
    return -1


def compute_category(event, user):
    print(event.category)
    weights = {
        'music': user.music,
        'visual-arts': user.visual,
        'performing-arts': user.performing,
        'film': user.film,
        'lectures-books': user.lectures,
        'fashion': user.fashion,
        'food-and-drink': user.food,
        'charities': user.charity,
        'sports-active-life': user.sports,
        'nightlife': user.nightlife,
        'kids-family': user.family,
        'festival-fairs': user.festivals
    }
    try:
        if event.temporary:
            return 1.5 * weights[event.category]
        return weights[event.category]
    except KeyError:
        return 3


def compare_cost(event, max_cost):
    if event.cost > max_cost:
        return 0
    else:
        return 1


def sort_events_by_time(event_list):
    return sorted(event_list, key=lambda e: e.start_time, reverse=True)


def get_temp_schedule(origin, event_list, user):
    events = sort_events_by_time(event_list)
    t = TravelTimeMatrix(origin, events)
    n = len(events)
    optimal = [0] * (n + 1)
    optimal_list = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        previous_no_conflict_index = closest_non_conflict_index(t, i - 1)
        # previous_no_conflict_event = closest_non_conflict_event(t, i - 1)

        include_current = compute_category(events[i - 1], user)
        if previous_no_conflict_index >= 0:
            include_current += optimal[previous_no_conflict_index + 1]

        exclude_current = optimal[i - 1]
        if include_current > exclude_current:
            if previous_no_conflict_index >= 0:
                optimal_list[i].extend(optimal_list[previous_no_conflict_index + 1])
            optimal_list[i].append(events[i - 1])
            optimal[i] = include_current
        else:
            optimal_list[i].extend(optimal_list[i - 1])
            optimal[i] = exclude_current
    return optimal_list[n]

def schedule_empty_blocks(optimal_list, day_start, day_end):
    amended_schedule = []
    if len(optimal_list) == 0:
        amended_schedule.extend(recommend_places(day_start,day_end))
    else:
        prev = day_start
        for i in range(1,len(optimal_list)):
            print("thing")
            # if time range is >= 1 hour, look for events nearby and give top time/2 events





def find_place(blocks, prev_event, next_event):
    print("noting")
def recommend_places(day_start, day_end):
    print("noting")
    # get all events ranked based on categories for that day and display top 8

def create_blocks(start, end):
    block = []
    diff = end-start
    if diff.hour > 0:
        delta = datetime.timedelta(hour=2)
        curr_time = start
        while (end-curr_time).hour >= 4:
            block.append((curr_time , curr_time+delta))
            curr_time += delta
        block.append((curr_time, end))
    return block

def get_schedule(origin, event_list, user, day_start, day_end):
    s = get_temp_schedule(origin, event_list, user)
    empty_blocks = schedule_empty_blocks(s, day_start, day_end)
