from flask import Flask, render_template, request
from templates import api_connection 


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    match_id = (request.form['match_id'])

    team1_dict = api_connection.team1_id(match_id)
    team2_dict = api_connection.team2_id(match_id)

    team1_nickname = api_connection.team1_nicknames(match_id)
    team2_nickname = api_connection.team2_nicknames(match_id)


    return render_template('match.html', team1 = team1_nickname, team2 = team2_nickname)

if __name__ == '__main__':
    app.run(debug=True)