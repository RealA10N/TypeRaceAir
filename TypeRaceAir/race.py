# -- IMPORTS --#
import typing
import datetime


class Race():

    def __init__(self, sentence: str, players: typing.List[Player]):
        '''The race sentence'''
        self.sentence = sentence
        '''	The players that participate in the race.'''
        self._players = players
        self.__start_timestamp = datetime.datetime.now().timestamp()

    def log_result(self, player: Player, user_string: str):
        '''Logs the result of the given player.'''
        return PlayerRaceResult(race=self,
                                player=player,
                                submit_timestamp=datetime.datetime.now().timestamp(),
                                submit_sentence=user_string)


class Player():

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other

    def __ne__(self, other):
        return not self == other


class PlayerRaceResult():
    def __init__(self,
                 race: Race,
                 player: Player,
                 submit_timestamp: float,
                 submit_sentence: str
                 ):
        self.race = race
        self.submit_sentence = submit_sentence
        self.player = player
        self.submit_timestamp = submit_timestamp

    @property
    def words_mistake(self,) -> int:
        '''The number of words that the user typed incorrectly. '''
        return len(self.race.sentence.split()) - self.words_correct

    @property
    def words_correct(self,) -> int:
        '''The number of words that the user typed correctly. '''
        submitted_words = self.submit_sentence.split()
        target_words = self.race.sentence.split()
        return sum(
            1
            for cur_submitted, cur_target in zip(submitted_words, target_words)
            if cur_submitted == cur_target
        )

    @property
    def accuracy(self,) -> float:
        '''The percentage of words that the user typed correctly, out of the total words in the sentence. '''
        total_words = len(self.race.sentence.split())
        return self.words_correct / total_words

    @property
    def time(self,) -> float:
        '''The time that it took for the user to submit his answer, in seconds. '''
        return self.submit_timestamp - self.race.start_timestamp

    @property
    def wpm(self,) -> float:
        '''The WPM (Words Per Minute) of the current race for the current user. '''
        total_words = len(self.race.sentence.split())
        return (60 / self.time) * total_words

    @property
    def cwpm(self,) -> float:
        '''The CWPM (Correct Words Per Minute) of the current race for the current user. '''
        return (60 / self.time) * self.words_correct

    @property
    def score(self,) -> int:
        '''The total calculated score of the current player in the current race. '''
        return self.words_correct + (self.wpm * self.words_correct / 100)
