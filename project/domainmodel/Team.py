from __future__ import annotations
import Player
import TeamResult
import TeamFixture

class Team:
    def __init__(self, id: int, name: str, short_name: str, strength: int, code: int):
        self._id = id
        self._name = name
        self._short_name = short_name
        self._strength = strength
        self._code = code
        self._players = list() # one to many with Player
        self._results = list() # one to many with TeamResult
        self._fixtures = list() # one to many with TeamFixture

        # match stats
        self._played = 0
        self._wins = 0
        self._draws = 0
        self._losses = 0
        self._points = 0
        self._form = 0

        # goal stats
        self._gf = 0
        self._ga = 0
        self._gd = 0

    @property
    def id(self) -> int:
        return self._id
        
    @property
    def name(self) -> str:
        return self._name

    @property
    def short_name(self) -> str:
        return self._short_name
    
    @property
    def code(self) -> int:
        return self._code
    
    @property
    def players(self) -> list[Player.Player]:
        return self._players
    
    def add_player(self, player: Player.Player):
        self._players.append(player)
    
    # strength getters

    @property
    def strength(self) -> int:
        return self._strength
    
    # match stats getters and setters

    @property
    def played(self) -> int:
        return self._played
    
    @played.setter
    def played(self, new_played: int):
        self._played = new_played
    
    @property
    def wins(self) -> int:
        return self._wins
    
    @wins.setter
    def wins(self, new_wins: int):
        self._wins = new_wins
    
    @property
    def draws(self) -> int:
        return self._draws
    
    @draws.setter
    def draws(self, new_draws: int):
        self._draws = new_draws

    @property
    def losses(self) -> int:
        return self._losses
    
    @losses.setter
    def losses(self, new_losses: int):
        self._losses = new_losses
    
    @property
    def points(self) -> int:
        return self._points
    
    @points.setter
    def points(self, new_points: int):
        self._points = new_points
    
    @property
    def form(self) -> int:
        return self._form
    
    @form.setter
    def form(self, new_form: int):
        self._form = new_form

    # goal stats getters and setters

    @property
    def gf(self) -> int:
        return self._gf
    
    @gf.setter
    def gf(self, new_gf: int):
        self._gf = new_gf
    
    @property
    def ga(self) -> int:
        return self._ga
    
    @ga.setter
    def ga(self, new_ga: int):
        self._ga = new_ga
    
    @property
    def gd(self) -> int:
        return self._gd
    
    @gd.setter
    def gd(self, new_gd: int):
        self._gd = new_gd
    
    # results and fixtures getters and add methods

    @property
    def results(self) -> list[TeamResult.TeamResult]:
        return self._results
    
    def add_result(self, new_result: TeamResult.TeamResult):
        self._results.append(new_result)

        # update goals and xg
        self._gf += new_result.goals_scored
        self._ga += new_result.goals_conceded
        self._gd = self._gf - self._ga

        # update wins/losses, played, points
        self._played += 1
        if new_result.result == "Win":
            self._wins += 1
            self._points += 3
        elif new_result.result == "Loss":
            self._losses += 1
        else:
            self._draws += 1
            self._points += 1

        # update form
        total = 0
        if len(self._results) >= 5:
            for result in self._results[-5:]:
                total += result.points_gained
            form = total / 5
        else:
            i = 0
            for result in self._results:
                i += 1
                total += result.points_gained
            form = total / i
    
    @property
    def fixtures(self) -> list[TeamFixture.TeamFixture]:
        return self._fixtures
    
    def add_fixture(self, new_fixture: TeamFixture.TeamFixture):
        self._fixtures.append(new_fixture)

    # additional methods

    def __str__(self):
        return f"{self.id}. {self.name} ({self.short_name})"
    
    def __repr__(self):
        return f"{self.id}. {self.name} ({self.short_name})"