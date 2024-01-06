#!/usr/bin/python3
"""API Index Module"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

# Dictionary mapping endpoint names to corresponding model classes
classes = {"users": User, "places": Place, "states": State,
           "cities": City, "amenities": Amenity,
           "reviews": Review}

@app_views.route('/status', methods=['GET'])
def status():
    '''Route to retrieve API status'''
    return jsonify({'status': 'OK'})

@app_views.route('/stats', methods=['GET'])
def count():
    '''Retrieve the number of objects for each type'''
    count_dict = {}

    # Iterate through endpoint names and corresponding model classes
    for cls_key, cls_value in classes.items():
        count_dict[cls_key] = storage.count(cls_value)

    return jsonify(count_dict)
