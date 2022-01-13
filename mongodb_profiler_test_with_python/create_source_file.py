""" Creates source file with 500k records basedon 10k uuids"""
import json
import random
import string
from faker import Faker


def create_10k_uuid_list():
    """ This will bag of ids that will be re-used to insert records"""
    ids = []
    faker = Faker()
    for i in range(30000):
        ids.append(faker.uuid4())
    return ids


def create_500k_record_list():
    records = []
    ids = create_10k_uuid_list()
    faker = Faker()
    some_strings = string.ascii_lowercase
    for i in range(500000):
        random_date_time = faker.date_time_between(start_date='-1y', end_date='now').strftime('%Y-%m-%dT%H:%M:%S.%f%Z')
        records.append({
            "id": random.choice(ids),
            "date": {"created": random_date_time},
            "fname": ''.join(random.choices(some_strings, k=5)),
            "lname": ''.join(random.choices(some_strings, k=5))
        })
    return records


def write_records_to_file():
    """ """
    records = create_500k_record_list()
    with open('source_file.json', 'w') as file:
        json.dump(records, file, indent=2)
