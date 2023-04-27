python
import json
import boto3

def lambda_handler(event, context):
    
    # Create Kinesis stream client
    kinesis = boto3.client('kinesis')
    
    # Extract data from event object
    data = event['data']
    
    # Publish data to Kinesis stream
    response = kinesis.put_record(
        StreamName='my_stream',
        Data=data,
        PartitionKey='1'
    )
    
    # Log result
    print(f"Published data to Kinesis: {data}")
    
    # Return response
    return {
        'statusCode': 200,
        'body': json.dumps('Data published to stream')
    }
