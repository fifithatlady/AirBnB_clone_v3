#!/usr/bin/python3
<<<<<<< HEAD
"""index.py to connect to API"""
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage


hbnbText = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route('/status', strict_slashes=False)
def hbnbStatus():
    """hbnbStatus"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def hbnbStats():
    """hbnbStats"""
    return_dict = {}
    for key, value in hbnbText.items():
        return_dict[key] = storage.count(value)
    return jsonify(return_dict)

if __name__ == "__main__":
    pass
=======
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
>>>>>>> 36505c1647ff288e6c8ad4385e1e78c06ff9b35e
