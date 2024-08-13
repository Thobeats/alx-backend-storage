#!/usr/bin/env python3

import pymongo


def list_all(mongo_collection):
    doc = mongo_collection.find()
    if doc.count() == 0:
        return []
    return doc