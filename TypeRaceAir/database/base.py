""" This file contains the general implementation of the database in this
project. In general, there are two types of databases: the `ListDatabase` and
the `DictDatabase`. Both are stored in the local storage using `.json` files.
"""

import os
import atexit
import json
import random

from abc import ABC, abstractclassmethod


class BaseDatabase(ABC):
    """ Basic and general database. The other databases that the bot uses
    are based on this object. """

    def __init__(self, db_name: str):
        """ Loads the database with the given name. """

        self.name = db_name
        self._data = self.__load()
        atexit.register(self.save)  # Save databases when program exits

    @property
    @abstractclassmethod
    def EMPTY_DB(cls,):  # pylint: disable=invalid-name
        """ Abstract property. Returns the default (empty) database structure. """

    def __len__(self,):
        """ Returns the length of the database, as an integer (the amount of
        saved values in the database). """
        return len(self._data)

    # - - L O C A L - S T O R A G E - M A N A G M E N T - - #

    @property
    def filename(self,):
        """ Returns the database filename. """
        return self.name + '.json'

    @property
    def path(self,):
        """ Returns the path to the `.json` file that contains the current
        database. """

        return os.path.join(os.getcwd(), 'db', self.filename)

    def __load(self,):
        """ Loads the database from local storage. If database is not found,
        loads an empty database. """

        if not os.path.isfile(self.path):
            # If database file does not exist, loads and returns default
            # database
            return self.EMPTY_DB

        # If database found: opens and returns it.
        with open(self.path, 'r') as file:
            return json.load(file)

    def save(self,):
        """ Saves the database that is loaded in the memory to the local
        storage. """

        os.makedirs(os.path.dirname(self.path), exist_ok=True)

        with open(self.path, 'w') as file:
            json.dump(self._data, file)


class ListDatabase(BaseDatabase):
    """ This database saves cells by order - each cell has an index (integer)
    that represents its location in the database. You can access the recently
    added cell with the `-1` index, or the first cell in the database by the
    `0` index, etc. """

    EMPTY_DB = list()

    def get(self, index: int):
        """ Returns the cell that is saved in the given index in the list
        database. """
        return self._data[index]

    def get_last(self,):
        """ Returns the last (most recently added) cell from the list
        database. """
        return self.get(-1)

    def get_random(self,):
        """ Returns a random cell from the list database. """
        index = random.randint(0, len(self))
        return self.get(index)

    def add(self, **kwargs):
        """ Adds the given keyword arguments as a single cell to the
        database. """
        self._data.append(kwargs)

    def delete(self, index: int):
        """ Removes the cell in the given index from the database. """
        self._data.pop(index)


class DictDatabase(BaseDatabase):
    """ In this database structure, each cell has a and unique string. With this
    string, you can access, add, update or delete the cells. The cells are not
    saved in an order, and there is no 'first' or 'last' cell. """

    EMPTY_DB = dict()

    def get(self, key: str):
        """ Returns the value of the cell that is represented by the given key. """
        return self._data[key]

    def add(self, key: str, data):
        """ Adds the given data to the dict database, with the given key. """
        self._data[key] = data

    def delete(self, key: str):
        """ Removes the cell that is represented by the given key from the
        database. """
        del self._data[key]
