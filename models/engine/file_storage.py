#!/usr/bin/python3
"""
The file storage module
"""
import json
import os
from ..base_model import BaseModel
from ..user import User


class FileStorage:
    """
    class FileStorage that serializes instances to a
    JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = dict()
    classesDict = {'BaseModel': BaseModel, 'User': User}

    def __init__(self):
        ...

    def all(self):
        """
        returns the dictionary __objects
        """
        if FileStorage.__objects:
            return FileStorage.__objects
        else:
            return {}

    def new(self, obj):
        """
        sets in __objects the obj with
        key <obj class name>.id
        """
        if obj:
            key = f'{type(obj).__name__}.{obj.id}'
            FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to
        the JSON file (path: __file_path)
        """
        ObjectsWithDict = dict()
        newDict = dict()
        for key in FileStorage.__objects.keys():
            newDict = FileStorage.__objects[key].to_dict()
            ObjectsWithDict[key] = newDict
        with open(FileStorage.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(ObjectsWithDict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists,
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        dictsObjsDict = dict()
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as f:
                dictsObjsDict = json.load(f)
            for key, value in dictsObjsDict.items():
                obj = self.classesDict[value['__class__']](**value)
                self.__objects[key] = obj
            # note: to pass an argument as a keyword argument
            # put ** before it
            # We need to pass it as kwarg to make __init__ accept it
