
def my_cron_job():
    Event.objects.all().delete()
    for state in states.get_all_states().values():
        event_finder_object = event_finder.EventFinder(
            location=state,
            start_time=int(parser.parse(datetime.datetime.now().isoformat()).timestamp())
        )
        event_finder_object.save_all_events()
    # TODO stuff here
