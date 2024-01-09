#!/usr/bin/python3
"""Places-Amenities API views"""
from flask import jsonify, abort, make_response
from models import storage
from models.place import Place
from models.amenity import Amenity
from api.v1.views import app_views


@app_views.route('/places/<place_id>/amenities', methods=['GET'],
                strict_slashes=False)
def get_amenities_by_place(place_id):
    """Retrieves the list of all Amenity objects of a Place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    amenities = [amenity.to_dict() for amenity in place.amenities]
    return jsonify(amenities)


@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['DELETE'],
                strict_slashes=False)
def delete_amenity_from_place(place_id, amenity_id):
    """Deletes an Amenity object from a Place"""
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)

    if place is None or amenity is None or amenity not in place.amenities:
        abort(404)

    if storage.__class__.__name__ == 'DBStorage':
        place.amenities.remove(amenity)
        storage.save()
    else:  # Assuming it's FileStorage
        if amenity_id not in place.amenity_ids:
            abort(404)
        place.amenity_ids.remove(amenity_id)
        storage.save()

    return jsonify({})


@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['POST'],
                strict_slashes=False)
def link_amenity_to_place(place_id, amenity_id):
    """Links an Amenity object to a Place"""
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)

    if place is None or amenity is None:
        abort(404)

    if amenity in place.amenities:
        return jsonify(amenity.to_dict()), 200

    if storage.__class__.__name__ == 'DBStorage':
        place.amenities.append(amenity)
        storage.save()
    else:  # Assuming it's FileStorage
        if amenity_id in place.amenity_ids:
            return jsonify(amenity.to_dict()), 200
        place.amenity_ids.append(amenity_id)
        storage.save()

    return jsonify(amenity.to_dict()), 201
