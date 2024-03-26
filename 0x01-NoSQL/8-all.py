#!/usr/bin/env python3
""" List all document in python """

def list_all(mongo_collection):
    """ List all document in python

    :param mongo_collection:
    :return:
    """
    return mongo_collection.find()
