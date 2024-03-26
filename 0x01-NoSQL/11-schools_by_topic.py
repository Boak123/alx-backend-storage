#!/usr/bin/env python3
""" 
Where can i learn python
"""


def schools_by_topic(mongo_collection, topic):
    """ function that returns the list of school

    :param mongo_collection:
    :param topic:
    :return:
    """
    return mongo_collection.find({"topics": topic})
