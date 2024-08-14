#!/usr/bin/env python3
"""Mongo DB with PyMongo"""
from pymongo import MongoClient

if __name__ == "__main__":
    """ Statistics about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    num_of_logs = nginx_collection.count_documents({})
    print(f'{num_of_logs} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{status_check} status check')

    print('IPs:')
    top_ips = nginx_collection.aggregate([
        {"$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])

    for ips in top_ips:
        ip = ips.get("ip")
        count = ips.get("count")
        print(f'\t{ip}: {count}')
