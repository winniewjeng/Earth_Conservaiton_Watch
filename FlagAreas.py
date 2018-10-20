import re, sys, urllib.request, json, logging


class FlagAreas:

    def __init__(self, longitude=None, latitude=None):
        self.longitude = longitude
        self.latitude = latitude
