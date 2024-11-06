def lambda_handler(event, context):
    name = event.get('queryStringParameters', {}).get('name')
    
    if name:
        name_length = len(name)
        return {
            'statusCode': 200,
            'body': f'Name length is {name_length}'
        }
    else:
        return {
            'statusCode': 400,
            'body': 'Error: No name provided'
        }
