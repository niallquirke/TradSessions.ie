import json


def user_handler(event, context):
    print('Request:', event)
    response = {'status': 200, 'body': {'Message': 'Hiya'}}

    return {
        'statusCode': response['status'],
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True
        },
        'body': json.dumps(response['body'])
    }
