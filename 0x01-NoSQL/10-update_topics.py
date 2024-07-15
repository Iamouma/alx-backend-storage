#!/usr/bin/env python3
"""
MongoDB operations with python using pymongo
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on name
    """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, new_values)
