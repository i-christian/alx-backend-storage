#!/usr/bin/env python3
"""
.11-schools_by_topic.py
"""


def schools_by_topic(mongo_collection, topic):
    """
    schools_by_topic:
        args - mongo_collection
             - topic
        returns - the list of school
    """
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
