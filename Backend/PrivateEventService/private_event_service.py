import json
import boto3

EVENT_TABLE = 'tradsesh-0.1'
RANKING_TABLE = 'tradsesh-ranking-0.1'
USER_TABLE = 'tradsesh-UserTable'
EVENTS_PER_PAGE = 10

ddb_client = boto3.client('dynamodb')


##################
# Main Functions #
##################


def get_page(user, page):
    page = int(page)
    event_list = []
    event_ids = get_user_event_ids(user)
    for event_id in event_ids:
        event_list.append(get_event(event_id))
    return {'status': 200, 'body': {'events': event_list}}


def get_user_event_ids(user):
    ddb_event_ids = ddb_client.get_item(
        TableName=USER_TABLE, Key={'user': {'S': user}})
    if 'Item' in ddb_event_ids:
        return ddb_to_json(ddb_event_ids['Item'])['event_ids']
    else:
        return []


def get_event(event_id):
    ddb_event = ddb_client.get_item(
        TableName=EVENT_TABLE, Key={'id': {'S': event_id}})
    return ddb_to_json(ddb_event['Item'])


def create_event(event):
    event = json.loads(event)
    number_of_events = len(ddb_client.scan(TableName=RANKING_TABLE)['Items'])
    ddb_client.put_item(
        TableName=EVENT_TABLE,
        Item=json_to_ddb_event(event)
    )
    ddb_client.put_item(
        TableName=RANKING_TABLE,
        Item=json_to_ddb_rank(event, number_of_events)
    )
    ddb_user = ddb_client.get_item(
        TableName=USER_TABLE,
        Key={'user': {'S': event['user']}}
    )
    print(ddb_user)
    if 'Item' in ddb_user:
        user = ddb_to_json(ddb_user['Item'])
        print(user)
        user['event_ids'].append(event['id'])
        print(str(user['event_ids']))
        ddb_client.put_item(
            TableName=USER_TABLE,
            Item=json_to_ddb_user(event['user'], user['event_ids'])
        )
    else:
        ddb_client.put_item(
            TableName=USER_TABLE,
            Item=json_to_ddb_user(event['user'], [event['id']])
        )
    return {'status': 200, 'body': {'Message': 'Successfully created event'}}


#####################
# Dynamo Formatting #
#####################


def ddb_to_json(node):
    data = dict({})
    data['M'] = node
    return _unmarshal_value(data)


def _unmarshal_value(node):
    if type(node) is not dict:
        return node
    for key, value in node.items():
        key = key.lower()
        if key == 'bool':
            return value
        if key == 'null':
            return None
        if key == 's':
            return value
        if key == 'n':
            if '.' in str(value):
                return float(value)
            return int(value)
        if key in ['m', 'l']:
            if key == 'm':
                data = {}
                for key1, value1 in value.items():
                    if key1.lower() == 'l':
                        data = [_unmarshal_value(n) for n in value1]
                    else:
                        if type(value1) is not dict:
                            return _unmarshal_value(value)
                        data[key1] = _unmarshal_value(value1)
                return data
            data = []
            for item in value:
                data.append(_unmarshal_value(item))
            return data


def json_to_ddb_event(event):
    return {
        'id': {'S': event['id']},
        'user': {'S': event['user']},
        'title': {'S': event['title']},
        'craic': {'S': event['craic']},
        'location': {'S': event['location']},
        'day': {'S': event['day']},
        'time': {'S': event['time']},
        'county': {'S': event['county']}
    }


def json_to_ddb_rank(event, number_of_events):
    return {
        'rank': {'N': str(number_of_events)},
        'id': {'S': event['id']}
    }


def json_to_ddb_user(user, event_ids):
    ddb_event_ids = []
    for event_id in event_ids:
        ddb_event_ids.append({'S': event_id})
    print(ddb_event_ids)
    return {
        'user': {'S': user},
        'event_ids': {'L': ddb_event_ids}
    }


###############
# Entry Point #
###############


def private_event_handler(event, context):
    print('Request', event)
    response = {'status': 400, 'body': {'Error': 'Invalid http method'}}

    if event['httpMethod'] == 'GET':
        if event['queryStringParameters']:
            params = event['queryStringParameters']
            if 'user' in params and 'page' in params:
                response = get_page(params['user'], params['page'])
            else:
                response = {'status': 400, 'body': {
                    'Error': 'Invalid query string parameters'}}
        else:
            response = {'status': 400, 'body': {
                'Error': 'No query string found'}}

    elif event['httpMethod'] == 'POST':
        response = create_event(event['body'])

    return {
        'statusCode': response['status'],
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Credentials': True
        },
        'body': json.dumps(response['body'])
    }
