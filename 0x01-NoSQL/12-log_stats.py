#!/usr/bin/env python3
""" 12. Log stats
"""

from pymongo import MongoClient

def log_stats():
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client['logs']['nginx']

    total = logs_collection.count_documents({})
    
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: logs_collection.count_documents({"method": method}) for method in methods}

    path_status_count = logs_collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{total} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{path_status_count} status check")

if __name__ == "__main__":
    log_stats()
