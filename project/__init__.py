"""
Initialize the flask app
"""

from flask import Flask

def create_app():
    app = Flask(__name__, template_folder="project/templates")

    with app.app_context():
        # register blueprints
        pass

    return app

# create a dictionary of the 20 teams with keys as ids (teams_dict)
# create a list of all players (test_players)
# each team has a list of players, each player has a reference to its team

# go through fixtures api, create a dictionary for each team
# value of dict is list of fixture ids of results
# also create TeamResult and TeamFixture objects
# then for each player go through ["history"] mapping fixture ids to results