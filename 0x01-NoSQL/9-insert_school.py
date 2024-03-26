#!/usr/bin/env python3
""" Insert a document in python """


def insert_school(mongo_collection, **kwargs):
    """ Insert a document in python

    :param mongo_collection:
    :param **kwargs:
    :return:
    """
    new_document = mongo_collection,insertOne(kwargs)
    return new_document.inserted_id
