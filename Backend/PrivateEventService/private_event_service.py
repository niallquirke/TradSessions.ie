import json


def private_event_handler(event, context):
    print('Request:', event)
    response = {'status': 200, 'body': {"events": [{"location": "Walshes, StoneyBatter, Dublin 7", "county": "Dublin", "comments": ["Niall Quirke", "Aimee Crawford"], "user": {"name": "Lisa O'Neill", "id": "cba123"}, "time": "9pm", "day": "Sundays", "description": "Too advanced to join in but your ears will melt with happiness!", "id": "5928101", "rank": 0, "title": "Lisa O'Neill and Friends"}, {
        "location": "McNeill's, Capel Street, Dublin 7", "county": "Dublin", "comments": ["Shauna", "Maria", "Laura Quirke"], "user": {"name": "Fiacra Meek", "id": "abc123"}, "time": "7pm", "day": "Fridays", "description": "A session for anyone to join!", "id": "8419988", "rank": 1, "title": "McNeill's"}], "last_page": True}}

    return {
        'statusCode': response['status'],
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Credentials": True
        },
        'body': json.dumps(response['body'])
    }
