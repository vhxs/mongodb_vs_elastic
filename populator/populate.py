import random
import hashlib
from pymongo import MongoClient
from elasticsearch import Elasticsearch
import time

def generate_int_list():
    size = random.randint(0, 2000)
    return [random.randint(0, 1000000) for _ in range(size)]

def populate_forever():
    mongo_client = MongoClient('mongodb')
    es_client = Elasticsearch("http://elasticsearch:9200")

    while True:
        document_id = hashlib.sha256(f"{str(time.time())}".encode("utf8")).hexdigest()
        int_list = generate_int_list()
        mongo_document = {"_id": document_id, "stuff": int_list}
        mongo_client['test']['documents'].insert_one(mongo_document)
        es_document = {"stuff": int_list}
        es_client.index(index="documents", document=es_document)

populate_forever()