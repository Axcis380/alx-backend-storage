#!/usr/bin/env python3
""" Performing MongoDB operations in Python using pymongo """


def insert_school(mongo_collection, **kwargs):
    """ Add a new document to a collection using kwargs """
    document_id = mongo_collection.insert(kwargs)
    return document_id
