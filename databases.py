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


class BaseDatabase:
    """ Basic and general database. The other databases that the bot uses
    are based on this object. """


class StatsDatabase(BaseDatabase):
    """ Saves general information (total races, players played, etc.) """


class UsersDatabase(BaseDatabase):
    """ Saves information about individual users, and information about the last
    N races of the user. """


class StringsDatabase(BaseDatabase):
    """ A base object that is used by the `SubmittedStringsDatabase` and the
    `ApprovedStringsDatabase`. """


class ApprovedStringsDatabase(StringsDatabase):
    """ A database that saves a list of the manually approved racing strings. """


class SubmittedStringsDatabase(StringsDatabase):
    """ A database that saves a list of the submitted (but not yet approved) racing
    strings. """
