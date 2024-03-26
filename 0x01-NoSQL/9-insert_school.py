#!/usr/bin/env python3
""" Insert a document in python """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a document in python in a 
    collection based on kwargs

    
    :param mongo_collection:
    :param **kwargs:
    :return:
    """
    new_documents = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
