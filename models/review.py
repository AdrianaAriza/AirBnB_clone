#!/usr/bin/python3
"""
Review Module

"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review City """
    place_id = ""
    user_id = ""
    text: ""

    def __init__(self, **kwargs):
        super().__init__()