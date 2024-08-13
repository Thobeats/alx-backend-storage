#!/usr/bin/env python3
"""Mongo DB with PyMongo"""


def insert_school(mongo_collection, **kwargs):
    """ Insert a new document to the collection """
    return mongo_collection.insert(kwargs)
         