from __future__ import annotations
import Player
import TeamResult

class PlayerResult:
    def __init__(self, player: Player.Player, team_result: TeamResult.TeamResult, gameweek: int, 
                 minutes: int, home: bool, goals: int, assists: int, xg: float, 
                 xa: float, points: int, saves: int = 0, yellow_card: bool = False, 
                 red_card: bool = False, penalties_saved: int = 0, penalties_missed: int = 0):
        self._player = player # many to one with Player
        self._result = team_result # many to one with TeamResult
        self._gameweek = gameweek
        self._minutes = minutes 
        self._home = home # true if home fixture else false for 
        
        # stat fields
        self._goals = goals
        self._assists = assists
        self._xg = xg
        self._xa = xa
        self._points = points
        self._penalties_missed = penalties_missed

        # cards (true or false)
        self._yellow_card = yellow_card
        self._red_card = red_card

        # goalkeepers
        self._saves = saves
        self._penalties_saved = penalties_saved

    # Getters
    @property
    def player(self) -> Player:
        return self._player

    @property
    def result(self) -> TeamResult:
        return self._result

    @property
    def gameweek(self) -> int:
        return self._gameweek

    @property
    def minutes(self) -> int:
        return self._minutes

    @property
    def home(self) -> bool:
        return self._home

    @property
    def goals(self) -> int:
        return self._goals

    @property
    def assists(self) -> int:
        return self._assists

    @property
    def xg(self) -> float:
        return self._xg

    @property
    def xa(self) -> float:
        return self._xa

    @property
    def points(self) -> int:
        return self._points

    @property
    def penalties_missed(self) -> int:
        return self._penalties_missed

    @property
    def yellow_card(self) -> bool:
        return self._yellow_card

    @property
    def red_card(self) -> bool:
        return self._red_card

    @property
    def saves(self) -> int:
        return self._saves

    @property
    def penalties_saved(self) -> int:
        return self._penalties_saved