#!/usr/bin/python3
"""Defines class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents Review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes Review"""
        super().__init__(*args, **kwargs)
