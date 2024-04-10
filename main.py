from flask import Flask, render_template, request
from templates import api_connection 
from time import time
from collections import defaultdict
import asyncio
import aiohttp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    #form that requests match id
    match_id = (request.form['match_id'])

    #match data that is got from get_match_data api call
    match_data = api_connection.get_match_data(match_id)

    #player id and rank from match data
    player_id_and_rank = api_connection.get_player_id_and_rank(match_id)

    #stores the teams player id's
    team1_player_ids = []
    team2_player_ids = []

    #grabs the teams player id's
    for player_data in player_id_and_rank['team1_data'].values():
        team1_player_ids.append(player_data[1])
    
    for player_data in player_id_and_rank['team2_data'].values():
        team2_player_ids.append(player_data[1])

    team1_data = api_connection.win_rate_overall(team1_player_ids)

    team1_winrates = []

    for item in team1_data:
        team1_winrates.append(item['lifetime']['Win Rate %'])

    team2_data = api_connection.win_rate_overall(team2_player_ids)

    team2_winrates = []

    for item in team2_data:
        team2_winrates.append(item['lifetime']['Win Rate %'])





    return render_template('match.html',player_id_and_rank = player_id_and_rank, 
                           team1_player_ids = team1_player_ids, team1_winrates = team1_winrates,
                           team2_winrates = team2_winrates)


if __name__ == '__main__':
    app.run(debug=True)
