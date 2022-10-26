#!/usr/bin/python3
"""Used as a storage linker between BaseModel to FileStorage
    Variable:
        storage
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
