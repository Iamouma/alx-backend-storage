#!/usr/bin/env python3
"""
import pymongo
"""


def list_all(mongo_collection):
    """
    lists all documents in Python
    """
    return [doc for doc in mongo_collection.find()]
