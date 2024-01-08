#!/usr/bin/python3
"""Initialize Blueprint for API views"""
from flask import Blueprint

# Create Blueprint instance with a URL prefix for all routes
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import all views for the Blueprint
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
from api.v1.views.places_amenities import *
