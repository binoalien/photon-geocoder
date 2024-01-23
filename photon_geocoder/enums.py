"""
Path: photon_geocoder/enums.py
"""
from enum import Enum


class Layer(str, Enum):
    HOUSE = "house"
    STREET = "street"
    LOCALITY = "locality"
    DISTRICT = "district"
    CITY = "city"
    COUNTY = "county"
    STATE = "state"
    COUNTRY = "country"
