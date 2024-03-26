#!/usr/bin/env python3
"""
.9-insert_school.py
"""


def insert_school(mongo_collection, **kwargs):
    """
    insert_school:
        args - mongo_collection
             - kwargs
        returns - the new _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
