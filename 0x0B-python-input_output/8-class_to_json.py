#!/usr/bin/python3
"""Contain a single funtion"""
import json


def class_to_json(obj):
    """Save json content to file"""
    jsonStr = (obj.__dict__)
    return jsonStr
