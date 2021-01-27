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

from .base import DictDatabase, ListDatabase


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
