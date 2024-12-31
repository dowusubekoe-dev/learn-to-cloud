import json
import boto3

def lambda_function.lambda_handler(event, context):
    try:
        # Extracting MovieID from query parameters
        movie_id = event['queryStringParameters'].get('MovieID')
        
        if not movie_id:
            return {
                'statusCode': 400,
                'body': json.dumps('MovieID is required')
            }
        
        # Logic to fetch movie data from DynamoDB (example)
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('Movies')  # Replace 'Movies' with your DynamoDB table name
        
        response = table.get_item(
            Key={'MovieID': movie_id}
        )
        
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps('Movie not found')
            }
        
        movie_data = response['Item']
        
        return {
            'statusCode': 200,
            'body': json.dumps(movie_data)
        }
        
    except Exception as e:
        # Log the error for debugging
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Internal server error: {str(e)}")
        }
