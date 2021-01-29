# -- IMPORTS --#
import typing
import time


class Race():

    def __init__(self, sentece: str, players: typing.List[Player]):
        '''The race sentence'''
        self.sentece = sentece
        '''	The players that participate in the race.'''
        self.players = players
        self.start_timestamp = None

    @property
    def _players(self,):
        '''A list of players that participate in the current race.'''
        pass

    @property
    def _is_over(self,) -> bool:
        '''checks if the race is over'''
        pass

    @property
    def __start_timestamp(self) -> None:
        ''' return the current timestamp from epoch '''
        return time.time()

    def log_result(self, player: Player, user_string: str):
        '''Logs the result of the given player.'''
        pass
        # return PlayerRaceResult(X, self.player, self.__start_timestamp, self.user_string)


class Player():
    @property
    def name(self, name: str) -> name:
        self.name = name

    def __eq__(self, other) -> bool:
        pass

    def __ne__(self, other):
        pass


class PlayerRaceResult():
    def __init__(self, race: Race, player: Player, submit_timestamp: float, submit_sentence: str):
        self.race = race
        self.submit_sentence = submit_sentence
        self.player = player
        self.submit_timestamp = submit_timestamp

    @property
    def words_mistake(self,) -> int:
        '''The number of words that the user typed incorrectly. '''
        return len(self.race.sentece.split()) - self.words_correct

    @property
    def words_correct(self,) -> int:
        '''The number of words that the user typed correctly. '''
        submitted_words = self.submit_sentence.split()
        target_words = self.race.sentece.split()
        return sum(
            1
            for cur_submitted, cur_target in zip(submitted_words, target_words)
            if cur_submitted == cur_target
        )

    @property
    def accuracy(self,) -> float:
        '''The percentage of words that the user typed correctly, out of the total words in the sentence. '''
        total_words = len(self.race.sentece.split())
        return self.words_correct/total_words

    @property
    def time(self,) -> float:
        '''The time that it took for the user to submit his answer, in seconds. '''
        return self.submit_timestamp - self.race.start_timestamp

    @property
    def wpm(self,) -> float:
        '''The WPM (Words Per Minute) of the current race for the current user. '''
        total_words = len(self.race.sentece.split())
        return (60/self.time)*total_words

    @property
    def cwpm(self,) -> float:
        '''The CWPM (Correct Words Per Minute) of the current race for the current user. '''
        return (60/self.time)*self.words_correct

    @property
    def score(self,) -> int:
        '''The total calculated score of the current player in the current race. '''
        return self.words_correct+(self.wpm*self.words_correct/100)