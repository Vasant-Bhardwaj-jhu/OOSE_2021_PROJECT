import requests
from dateutil import parser

from . import states

from ..models import Event


class Yelp:
    def __init__(self):
        self.BASE_URL = "https://api.yelp.com/v3/events"
        self.KEY = "rASKYiKqinQbxeQp7ccmL4rmNX6CaKOTKx5j0yNB8RpUVP3R7YMigSdpfmMLT9TmK91NrUyGrGKoHI-YANoUh5OKZW9O_N21QuzgQ5E2b2YHduJAe90L-D253ahbYXYx"
        self.HEADERS = {'Authorization': 'Bearer %s' % self.KEY}
        self.LIMIT = 50

    def parse_events(self, location, start_date_time):
        event_list = []
        print("starting")
        for i in range(3):
            params = {'location': location, 'limit': self.LIMIT, 'offset': i * self.LIMIT, 'start_date': start_date_time}

            request = requests.get(self.BASE_URL, params=params, headers=self.HEADERS)
            if request.status_code != 200:
                # print("ERROR")
                continue

            response = request.json()

            try:
                for event in response['events']:
                    e = Yelp.parse_one_event(event)
                    if e:
                        event_list.append(e)
            except KeyError:
                # print("Key error here")
                return []
        # print("Event list:")
        # print(event_list)
        return event_list

    @staticmethod
    def parse_one_event(event):
        new_event = Event()
        try:
            new_event.name = event['name']
            # print("name: " + new_event.name)

            # print("before time start")
            if event['time_start']:
                # new_event.start_time = parser.parse(event['dates']['start']['dateTime'])
                # start = parser.parse(event['time_start'])
                # print("time start")
                new_event.start_time = parser.parse(event['time_start']) # (start - start.utcoffset())
            else:
                # print("time start is no")
                return None
            # print("before time end")
            if event['time_end']:
                # print("time end is not none")
                # end = parser.parse(event['time_end'])
                new_event.end_time = parser.parse(event['time_end']) # (end - end.utcoffset())
            else:
                # print("time end is none")
                return None
            new_event.duration = new_event.end_time - new_event.start_time

            new_event.category = event['category'].lower()
            new_event.description = event['description']
            new_event.cost = float(event['cost']) if event['cost'] else 0
            new_event.picture = event['image_url']
            new_event.tickets = event['tickets_url']
            new_event.address1 = event['location']['address1']
            new_event.city = event['location']['city']
            state = states.get_state_code(event['location']['state'])
            if state:
                new_event.state = state
            else:
                return None
            new_event.country = event['location']['country']
            new_event.zip_code = event['location']['zip_code']
            # new_event.temporary = True
            # print("about to return")
            return new_event
        except KeyError:
            return None

