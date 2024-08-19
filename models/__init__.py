#!/usr/bin/python3
"""Initializes the package by importing filestorage"""
from models.engine.file_storage import FileStorage

"""instance of filestorage"""
storage = FileStorage()
storage.reload()
