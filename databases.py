""" This file manages the different databases that the bot uses on regular
bases.

The main dababases are:

1.  Stats Database:
    Saves general information (total races, players played, etc.)

2.  Users Database:
    Saves information about individual users, and information about the last
    N races of the user.

3.  Approved Strings Database:
    A database that saves a list of the manually approved racing strings.

4.  Submitted Strings Database:
    A database that saves a list of the submitted (but not yet approved) racing
    strings.

"""

import os
import atexit
import json
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

    EMPTY_DB = list()


class DictDatabase(BaseDatabase):

    EMPTY_DB = dict()


class StatsDatabase(DictDatabase):
    """ Saves general information (total races, players played, etc.) """


class UsersDatabase(DictDatabase):
    """ Saves information about individual users, and information about the last
    N races of the user. """


class StringsDatabase(ListDatabase):
    """ A base object that is used by the `SubmittedStringsDatabase` and the
    `ApprovedStringsDatabase`. """


class ApprovedStringsDatabase(StringsDatabase):
    """ A database that saves a list of the manually approved racing strings. """


class SubmittedStringsDatabase(StringsDatabase):
    """ A database that saves a list of the submitted (but not yet approved) racing
    strings. """
