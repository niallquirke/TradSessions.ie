import json
import boto3

INFO_TABLE = 'tradsesh-0.1'
RANKING_TABLE = 'tradsesh-ranking-0.1'
EVENTS_PER_PAGE = 8

client = boto3.client('dynamodb')
resource = boto3.resource('dynamodb')


def get_page(page):
    page = int(page)
    event_list = []
    last_page_flag = False
    i = ((page - 1) * EVENTS_PER_PAGE)
    while (i < page * EVENTS_PER_PAGE):
        id_response = get_event_id(i)
        if id_response['status'] == 200:
            event_response = get_event(id_response['body'])
            if event_response['status'] == 200:
                event_list.append(event_response['body'])
            else:
                return event_response
        i += 1
    if get_event_id(page * EVENTS_PER_PAGE)['status'] != 200:
        last_page_flag = True
    return {'status': 200, 'body': {"events": event_list, "last_page": last_page_flag}}


def get_event_id(rank):
    try:
        dynamo = client.get_item(TableName=RANKING_TABLE, Key={
                                 'rank': {'N': str(rank)}})
        return {'status': 200, 'body': unmarshal_dynamodb_json(dynamo['Item'])['id']}
    except:  # noqa E722
        err = 'No event found for rank ' + str(rank)
        print('Error:', err)
        return {'status': 404, 'body': {'Error': err}}


def get_event(event_id):
    try:
        dynamo = client.get_item(TableName=INFO_TABLE, Key={
                                 'id': {'S': event_id}})
        return {'status': 200, 'body': unmarshal_dynamodb_json(dynamo['Item'])}
    except:  # noqa E722
        err = 'Event ID "' + event_id + '" was in the ranking table but not the event table'
        print('Error:', err)
        return {'status': 404, 'body': {'Error': err}}


def unmarshal_dynamodb_json(node):
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


def public_event_handler(event, context):
    print('Request', event)
    response = {'status': 400, 'body': {'Error': 'Invalid http method'}}

    if event['httpMethod'] == 'GET':
        if event['queryStringParameters']:
            if 'page' in event['queryStringParameters']:
                response = get_page(event['queryStringParameters']['page'])
            elif 'id' in event["queryStringParameters"]:
                response = get_event(event["queryStringParameters"]['id'])
            else:
                response = {'status': 400, 'body': {
                    'Error': 'Invalid parameter'}}
        else:
            response = {'status': 400, 'body': {
                'Error': 'No query string found'}}

    return {
        'statusCode': response['status'],
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True
        },
        'body': json.dumps(response['body'])
    }
