#!/usr/bin/env python3
"""
.8-all.py
"""


def list_all(mongo_collection):
    """
    list_all:
        args - mongo_collection
        returns -  a list of all docs in a collection
    """
    return [doc for doc in mongo_collection.find()]
