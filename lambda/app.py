import json

def lambda_handler(event, context):
    print("Hello World")
    vFinalMsg = "Done"
    return {
        'statusCode': 200,
        'body': vFinalMsg
    }
