#!/usr/bin/env python3
""" Performing MongoDB Operations in Python using pymongo """


def schools_by_topic(mongo_collection, topic):
    """ Retrieve the list of schools that have a specific topic """
    documents = mongo_collection.find({"topics": topic})
    list_docs = [d for d in documents]
    return list_docs
