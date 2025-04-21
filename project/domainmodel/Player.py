from __future__ import annotations
import Team
import PlayerResult

class Player:
    def __init__(self, id: int, position: str, name: str, first_name: str,
                 last_name: str, code: str, photo: str, team: Team.Team):
        self._id = id
        self._position = position
        self._first_name = first_name
        self._last_name = last_name
        self._name = name
        self._code = code
        self._team = team # one to one with Team

        # point stats
        self._total_points = 0
        self._form = 0

        # stats
        self._goals = 0
        self._xg = 0
        self._assists = 0
        self._xa = 0
        self._minutes = 0

        # goalkeepers
        self._saves = 0
        self._penalties_saved = 0

        # transfer stats
        # may take this as a a parameter as well
        self._transfers_in = 0
        self._transfers_out = 0

        self._results = list() # one to many with PlayerResult

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def position(self) -> str:
        return self._position
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def first_name(self) -> str:
        return self._first_name
    
    @property
    def last_name(self) -> str:
        return self._last_name
    
    @property
    def code(self) -> str:
        return self._code
    
    @property
    def team(self) -> Team.Team:
        return self._team
    
    # point fields getters

    @property
    def total_points(self) -> int:
        return self._total_points

    @property
    def form(self) -> float:
        return self._form
    
    # stat fields getters
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
    def minutes(self) -> int:
        return self._minutes
    
    # transfer stat fields getters

    @property
    def transfers_in(self) -> int:
        return self._transfers_in
    
    @property
    def transfers_out(self) -> int:
        return self._transfers_out
    
    # result list getter

    @property
    def results(self) -> list[PlayerResult.PlayerResult]:
        return self._results
    
    def add_result(self, new_result: PlayerResult.PlayerResult):
        self._results.append(new_result)

        # update stats
        self._goals += new_result.goals
        self._assists += new_result.assists
        self._xg += new_result.xg
        self._xa += new_result.xa
        self._total_points += new_result.points
        self._penalties_saved += new_result.penalties_saved
        self._saves += new_result._saves
        self._minutes += new_result.minutes

        # update form
        total = 0
        if len(self._results) >= 5:
            for result in self._results[-5:]:
                total += result.points
            form = total / 5
        else:
            i = 0
            for result in self._results:
                i += 1
                total += result.points
            form = total / i
    
    # other methods

    def __str__(self):
        return f"{self._name} ({self._team._name})"
    
    def __repr__(self):
        return f"{self._name} ({self._team._name})"