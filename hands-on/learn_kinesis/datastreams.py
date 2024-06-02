import boto3
import json
from datetime import datetime
import calendar
import random
import time
import json
from faker import Faker
import uuid
from time import sleep

my_stream_name = 'cw-kinesis1'

kinesis_client = boto3.client('kinesis',
                              region_name='ap-northeast-2',
                              aws_access_key_id='',
                              aws_secret_access_key=''
                              )
faker = Faker()

for i in range(1, 10):
    json_data = {
        "name":faker.name(),
        "city":faker.city(),
        "phone":faker.phone_number(),
        "id":uuid.uuid4().__str__()
    }
    print(json_data)
    sleep(0.5)

    put_response = kinesis_client.put_record(
        StreamName=my_stream_name,
        Data=json.dumps(json_data),
        PartitionKey='name')
    print(put_response)




