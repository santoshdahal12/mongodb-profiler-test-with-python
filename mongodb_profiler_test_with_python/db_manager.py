import json
import os
import dateutil.parser
from pymongo.errors import BulkWriteError
from pymongo import MongoClient, DESCENDING

client = MongoClient(host='localhost', port=27017)
database = client.testdatabase
collection = database.records_collection


def split_to_chunks(records, split_size=1000):
    for record in range(0, len(records), split_size):
        yield records[record:record + split_size]


def parse_date_time(record):
    """parse datetime stamp in str before writing to mongo"""
    date_time_stamp = record['date']['created']
    record['date']['created'] = dateutil.parser.parse(date_time_stamp)
    return record


def insert_bulk():
    with open('source_file.json') as file:
        records = json.load(file)
        total_records_with_same_id = set(map(lambda x: x['id'], records))
        datetime_parsed_records = [parse_date_time(r) for r in records]
        print(f"total records with same id in 500k records are: {len(total_records_with_same_id)}")
        splits_for_insert = list(split_to_chunks(datetime_parsed_records))
        print(len(splits_for_insert))
        for split in splits_for_insert:
            try:
                collection.insert_many(split)
            except BulkWriteError as ex:
                print(ex)


def fine_by_id(id):
    record = collection.find_one({'id': id}, {"_id": 0}, sort=[("date.created", DESCENDING)])
    return record


def fine_by_date(date):
    records = collection.find({'date.created': date})
    for record in records:
        print(record)
