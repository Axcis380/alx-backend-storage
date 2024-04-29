#!/usr/bin/env python3
""" Performing MongoDB Operations in Python with pymongo """


def update_topics(mongo_collection, name, topics):
    """ Modifying all topics in a school document based on their name """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, new_values)
