# FPLense
A web application built with Flask that pulls live Fantasy Premier League data through the FPL API. It displays player and team stats, allowing userxplos to ere the top performers and view detailed player information. Perfect for scouting players and building your FPL squad!

## Installation

**Installation via requirements.txt**

**Windows**
```shell
$ cd <project directory>
$ python3 -m venv venv
$ venv/Scripts/activate
$ pip install -r requirements.txt
```

**MacOS**
```shell
$ cd <project directory>
$ python3 -m venv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
```

## Execution

**Running theapplication**
From the *project directory* and within the activated virtual environment:
````shell
$ flask run
````

## Testing

## Configuration

## Data sources

The data for this application comes from the official FPL API:
base: https://fantasy.premierleague.com/api/
static data: https://fantasy.premierleague.com/api/bootstrap-static/
fixture data: https://fantasy.premierleague.com/api/fixtures/
gameweek data: https://fantasy.premierleague.com/api/event/{gameweek_number}/live/
detailed player stats: https://fantasy.premierleague.com/api/element-summary/{player_id}/
