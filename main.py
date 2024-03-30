from flask import Flask, render_template, request
from templates import api_connection 


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
    player_id_and_rank = api_connection.get_player_id_and_rank(match_data)

    return render_template('match.html',player_id_and_rank = player_id_and_rank )


if __name__ == '__main__':
    app.run(debug=True)
