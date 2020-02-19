import json


def log_event(event):
    print("#" * 100)
    event_json = json.dumps(event, indent=4, sort_keys=False)
    print("#---- event:", event_json)
    print("#" * 100)
