import requests

key = "fde1c0a3-1e2c-4c2e-a982-8d851b6c43d9"
match_id = "1-1c9a7df8-73b7-4796-b86f-7e42da3f3d2d"

nick_name = "david-deagle"

# response = requests.get(
#     'https://open.faceit.com/data/v4/matches/1-1c9a7df8-73b7-4796-b86f-7e42da3f3d2d',
#     headers={'Authorization': 'Bearer fde1c0a3-1e2c-4c2e-a982-8d851b6c43d9'})

# player id 
# 3137eb0b-7901-4783-9480-daced3aad07d


def get_player_id_and_rank(nick_name):

    response = requests.get(
    'https://open.faceit.com/data/v4/players?nickname=' + nick_name + '&game=cs2',
    headers={'Authorization': 'Bearer fde1c0a3-1e2c-4c2e-a982-8d851b6c43d9'})
    
    json_data = response.json()

    player = {}

    player['id'] = json_data['player_id']
    player['skill_level'] = json_data['games']['cs2']['skill_level']
    player['elo'] = json_data['games']['cs2']['faceit_elo']

    return player
 

def team1_id(match_id):
    
    response = requests.get(
    'https://open.faceit.com/data/v4/matches/' + match_id,
    headers={'Authorization': 'Bearer fde1c0a3-1e2c-4c2e-a982-8d851b6c43d9'})
    

    json_data = response.json()

    team1 = json_data['teams']['faction1']['roster']
    team1_ids = {}
    
    for i in range(len(team1)):
        display_name = team1[i]['nickname']
        player_id =team1[i]['game_player_id']
        team1_ids[display_name] = player_id

    return team1_ids

def team2_id(match_id):

    response = requests.get(
    'https://open.faceit.com/data/v4/matches/' + match_id,
    headers={'Authorization': 'Bearer fde1c0a3-1e2c-4c2e-a982-8d851b6c43d9'})

    json_data = response.json()

    team2 = json_data['teams']['faction2']['roster']
    team2_ids = {}

    for i in range(len(team2)):
        display_name =team2[i]['nickname']
        player_id = team2[i]['game_player_id']
        team2_ids[display_name] = player_id

    return team2_ids

def team1_nicknames(match_id):
    response = requests.get(
    'https://open.faceit.com/data/v4/matches/' + match_id,
    headers={'Authorization': 'Bearer fde1c0a3-1e2c-4c2e-a982-8d851b6c43d9'})

    json_data = response.json()

    team1 = json_data['teams']['faction1']['roster']
    team1_nicknames = []

    for i in range(len(team1)):
        display_name =team1[i]['nickname']
        team1_nicknames.append(display_name)

    return team1_nicknames

def team2_nicknames(match_id):
    response = requests.get(
    'https://open.faceit.com/data/v4/matches/' + match_id,
    headers={'Authorization': 'Bearer fde1c0a3-1e2c-4c2e-a982-8d851b6c43d9'})

    json_data = response.json()

    team2 = json_data['teams']['faction2']['roster']
    team2_nicknames = []

    for i in range(len(team2)):
        display_name =team2[i]['nickname']
        team2_nicknames.append(display_name)

    return team2_nicknames


def win_rate_overall(player_id):
    response = requests.get(
    'https://open.faceit.com/data/v4/players/' + player_id + '/stats/cs2',
    headers={'Authorization': 'Bearer fde1c0a3-1e2c-4c2e-a982-8d851b6c43d9'})

    json_data = response.json()

    overall_winrate = json_data['lifetime']['Win Rate %']
    return overall_winrate

    
def win_rate_by_map(player_id):
    response = requests.get(
    'https://open.faceit.com/data/v4/players/' + player_id + '/stats/cs2',
    headers={'Authorization': 'Bearer fde1c0a3-1e2c-4c2e-a982-8d851b6c43d9'})

    json_data = response.json()

    map_pool = ['Anubis', 'Mirage', 'Ancient', 'Inferno', 'Nuke', 'Overpass', 'Vertigo']
    winrate_map_dict = {}

    for i in range(len(json_data['segments'])):
        winrate_map_dict[map_pool[i]] = json_data['segments'][i]['stats']['Win Rate %']

    return winrate_map_dict

def player_stats(player_id):
    response = requests.get(
    'https://open.faceit.com/data/v4/players/' + player_id + '/stats/cs2',
    headers={'Authorization': 'Bearer fde1c0a3-1e2c-4c2e-a982-8d851b6c43d9'}
    )

    json_data = response.json()

    stats = {}

    stats['average_kd'] = json_data['lifetime']['Average K/D Ratio']
    stats['average_hs'] = json_data['lifetime']['Average Headshots %']


