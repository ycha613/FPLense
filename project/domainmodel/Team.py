from __future__ import annotations

class Team:
    def __init__(self, id: int, name: str, short_name: str, strength: int, code: int,
                 strength_overall_home: int, strength_overall_away: int, strength_attack_home: int,
                 strength_attack_away: int, strength_defence_home: int, strength_defence_away: int):
        self._id = id
        self._name = name
        self._short_name = short_name
        self._strength = strength
        self._code = code

        # strength
        self._strength_overall_home = strength_overall_home
        self._strength_overall_away = strength_overall_away
        self._strength_attack_home = strength_attack_home
        self._strength_attack_away = strength_attack_away
        self._strength_defence_home = strength_defence_home
        self._strength_defence_away = strength_defence_away

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

        # results and fixtures lists
        self._results = list()
        self._fixtures = list()

    @property
    def id(self) -> int:
        return self._id
        
    @property
    def name(self) -> str:
        return self._name

    @property
    def short_name(self) -> str:
        return self._id
    
    @property
    def code(self) -> int:
        return self._code
    
    # strength getters

    @property
    def strength(self) -> int:
        return self._strength
    
    @property
    def strength_overall_home(self) -> int:
        return self._strength_overall_home
    
    @property
    def strength_overall_away(self) -> int:
        return self._strength_overall_away
    
    @property
    def strength_attack_home(self) -> int:
        return self._strength_attack_home
    
    @property
    def strength_attack_away(self) -> int:
        return self._strength_attack_away
    
    @property
    def strength_defence_home(self) -> int:
        return self._strength_defence_home
    
    @property
    def strength_defence_away(self) -> int:
        return self._strength_defence_away
    
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
    def results(self) -> []:
        return self._results
    
    def add_result(self):
        pass
    
    @property
    def fixtures(self) -> []:
        return self._fixtures
    
    def add_fixture(self):
        pass

    # additional methods

    def __str__(self):
        return f"{self.id}. {self.name} ({self.short_name})"
    
    def __repr__(self):
        return f"{self.id}. {self.name} ({self.short_name})"