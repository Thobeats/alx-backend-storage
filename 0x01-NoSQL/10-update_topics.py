#!/usr/bin/env python3
"""Mongo DB with PyMongo"""


def update_topics(mongo_collection, name, topics):
    """ Update a document in the collection """
    mongo_collection.update_many({"name": name},
                            {"$set": {"topics": topics}})
