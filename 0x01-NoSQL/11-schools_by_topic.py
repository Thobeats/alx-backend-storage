#!/usr/bin/env python3
"""Mongo DB with PyMongo"""


def schools_by_topic(mongo_collection, topic):
    """ Get all documents that have a specific topic """
    mongo_collection.find({"topics": topic})
