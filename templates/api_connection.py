import requests
import asyncio
import aiohttp
from dotenv import load_dotenv
import os

load_dotenv('.env')
key: str = os.getenv('API_KEY')

#This function will retrieve [Player names, Player id's, Faceit ranks, avatars, win probablility] data
def get_match_data(match_id):
    response = requests.get(
    'https://open.faceit.com/data/v4/matches/' + str(match_id),
    headers={'Authorization': 'Bearer ' + key}        
    )

    json_data = response.json()

    return json_data

def get_player_data(player_id):
    response = requests.get(
    'https://open.faceit.com/data/v4/players/' + player_id + '/stats/cs2',
    headers={'Authorization': 'Bearer ' + key}  
    )

    json_data = response.json()

    return json_data

#This function will parse get_match_data and return [Player_id and rank]
def get_player_id_and_rank(match_id):
    json_data = get_match_data(match_id)

    loaded_data = {}

    team1 = json_data['teams']['faction1']['roster']
    print(team1)
    team2 = json_data['teams']['faction2']['roster']
    team1_ids = {}
    team2_ids = {}
    
    for i in range(len(team1)):
        display_name = team1[i]['nickname']
        player_id =team1[i]['player_id']
        skill_level = team1[i]['game_skill_level']
        avatar = team1[i]['avatar']
        team1_ids[f'Player{i}'] = [display_name, player_id, skill_level, avatar]

    for i in range(len(team2)):
        display_name = team2[i]['nickname']
        player_id =team2[i]['player_id']
        skill_level = team2[i]['game_skill_level']
        avatar = team2[i]['avatar']
        team2_ids[f'Player{i}'] = [display_name, player_id, skill_level, avatar]

    loaded_data["team1_data"] = team1_ids
    loaded_data["team2_data"] = team2_ids

    return loaded_data


def win_rate_overall(player_id_list):

    team1_player_ids = player_id_list
    team1_data = []

    def get_tasks(session):
            tasks = []
            for player in team1_player_ids:
                tasks.append(asyncio.create_task(session.get('https://open.faceit.com/data/v4/players/' 
                    + player + '/stats/cs2',
                    headers={'Authorization': 'Bearer fde1c0a3-1e2c-4c2e-a982-8d851b6c43d9'}, ssl = False)))
            return tasks

    async def get_winrate():
        async with aiohttp.ClientSession() as session:
            tasks = get_tasks(session)
            responses = await asyncio.gather(*tasks)
            for response in responses:
                team1_data.append(await response.json())

    asyncio.run(get_winrate())

    return team1_data



    
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


