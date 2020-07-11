import json


def log_event(event):
    print("#" * 100)
    event_json = json.dumps(event, indent=4, sort_keys=False)
    print("#---- event:", event_json)
    print("#" * 100)


def response(status_code, body=None):
    return {
        'statusCode': status_code,
        'body': body,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        }
    }
