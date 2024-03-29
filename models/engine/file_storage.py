#!/usr/bin/python3
""" defines a FileStroage class """
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Represent an abstracted storage engine.

Attributes:
    ___file_path (str): The name of the file to save objects to.
    ___objects (dict): A dictionary of instantiated objects.
"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary ___objects """
        return self.__objects

    def new(self, obj):
        """ sets in ___objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ saves objects into json file thats the ___file_path"""
        pdict = FileStorage.__objects
        obj_dict = {obj: pdict[obj].to_dict()
                    for obj in pdict.keys()
                    if isinstance(pdict[obj], BaseModel)}
        with open(FileStorage.__file_path, 'w+') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file ___file_path to ___objects,
        if it exists.
        """
        try:
            with open(self.__file_path, 'r') as f:
                dict = json.loads(f.read())
                for value in dict.values():
                    cls = value["__class__"]
                    del value["__class__"]
                    self.new(eval(cls)(**value))
        except FileNotFoundError:
            return
