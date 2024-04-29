#!/usr/bin/env python3
""" Performing MongoDB Operations in Python using pymongo """


def list_all(mongo_collection):
    """ Retrieve all documents using Python """
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents
