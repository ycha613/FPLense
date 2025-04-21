from __future__ import annotations
import Team

class TeamFixture:
    def __init__(self, team: Team.Team, opponent: Team.Team, date: str, home: bool):
        self._team = team # one to many with Team
        self._opponent = opponent # one to Many with Team
        self._date = date
        self._home = home

    @property
    def team(self) -> Team.Team:
        return self._team
    
    @property
    def opponent(self) -> Team.Team:
        return self._opponent
    
    @property
    def date(self) -> str:
        return self._date
    
    @property
    def home(self) -> bool:
        return self._home