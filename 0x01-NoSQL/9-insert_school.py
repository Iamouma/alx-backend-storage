#!/usr/bin/env python3
"""
import pymongo
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a nwe document in a collection based on kwargs
    """
    return mongo_collection.insert_one(kwargs).inserted_id
