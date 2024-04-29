#!/usr/bin/env python3
""" Executing MongoDB Operations in Python with pymongo """


def top_students(mongo_collection):
    """ Retrieve all students sorted by average score """

    top_st = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_st
