try:
    import re
    import os
    import json
    import boto3
    import datetime
    import uuid
    from datetime import datetime
    import json
    from faker import Faker
    import random
    import faker
except Exception as e:
    print("Error : {} ".format(e))


def main():
   

    AWS_ACCESS_KEY = " XXX"
    AWS_SECRET_KEY = "XXX"
    AWS_REGION_NAME = "ap-northeast-2"

    for i in range(1, 25):
        faker = Faker()
        json_data = {
            "name": faker.name(),
            "phone_numbers": faker.phone_number(),
            "city": faker.city(),
            "address": faker.address(),
            "date": str(faker.date()),
            "customer_id": str(random.randint(1, 5))
        }
        print(json_data)

        client = boto3.client(
            "firehose",
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name=AWS_REGION_NAME,
        )

        response = client.put_record(
            DeliveryStreamName='cw-kinesis1',
            Record={
                'Data': json.dumps(json_data)
            }
        )
        print(response)



main()

"""
customer_id=!{partitionKeyFromQuery:customer_id}/
"""
