import requests
import json

url = 'https://graphqlpokemon.favware.tech/v8'

headers = {
    'Content-Type':'application/json',
}

def dispatch(response, type):
    '''Utility to check for valid HTTP response code
    Args:
        response (HTTP response object): The HTTP response to dispatch
        type (str): The type of data to dispatch'''
    if response.status_code == 200:
        return response.json()['data'][type]
    else:
        raise Exception("API call failed with status code " + str(response.status_code))

def fetch_single_pokemon(name='dragonite'):
    '''Pass string with Pokemon name to call getPokemon(). Return response.json().
    Default: dragonite'''
    with open(f'./queries/extract_single_pokemon.gql', 'r') as file:
        query = ''.join(line for line in file if not line.strip().startswith('#'))

    variables= {
        'pokemon': name,
    }

    response = requests.post(url, json={'query':query, 'variables':variables}, headers=headers)
    return dispatch(response, 'getPokemon')

def fetch_all_pokemon(include_special=False):
    '''Fetch a list by calling getAllPokemon(). Return response.json().
    Optional parameter: include_special (default: False)'''
    with open(f'./queries/extract_pokemon.gql', 'r') as file:
        query = ''.join(line for line in file if not line.strip().startswith('#'))
    if not include_special:
        variables= {
            'offset':89
        }
    response = requests.post(url, json={'query':query, 'variables':variables if variables else None}, headers=headers)
    return dispatch(response, 'getAllPokemon')

def fetch_single_move(name='absorb'):
    '''Pass string with Move name to call getMove(). Return response.json().
    Default: absorb'''
    with open(f'./queries/extract_single_move.gql', 'r') as file:
        query = ''.join(line for line in file if not line.strip().startswith('#'))

    variables= {
        'move':name
    }
    response = requests.post(url, json={'query':query, 'variables':variables}, headers=headers)
    return dispatch(response, 'getMove')

def fetch_single_nature(name='jolly'):
    '''Pass string with Nature name to call getNature(). Return response.json().
    Default: jolly'''
    with open(f'./queries/extract_single_nature.gql', 'r') as file:
        query = ''.join(line for line in file if not line.strip().startswith('#'))

    variables= {
        'nature':name
    }
    response = requests.post(url, json={'query':query, 'variables':variables}, headers=headers)
    return dispatch(response, 'getNature')

def fetch_all_natures():
    '''Fetch a list by calling getAllNatures(). Return response.json().'''
    with open(f'./queries/extract_natures.gql', 'r') as file:
        query = ''.join(line for line in file if not line.strip().startswith('#'))

    response = requests.post(url, json={'query':query}, headers=headers)
    return dispatch(response, 'getAllNatures')

def fetch_type_matchup(primary_type='fire', secondary_type='ghost'):
    '''Pass a string primary_type and secondary_type to call getTypeMatchup(). Return response.json().
    Defaults:
        primary_type: fire
        secondary_type: ghost'''
    with open(f'./queries/extract_types.gql', 'r') as file:
        query = ''.join(line for line in file if not line.strip().startswith('#'))  
        variables = {
        'primaryType': primary_type.lower(),
        'secondaryType': secondary_type.lower()
        }
        response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)
    return dispatch(response, 'getTypeMatchup')

def fetch_all_moves():
    '''Fetch all available move names from the PokeAPI REST.'''
    url = 'https://pokeapi.co/api/v2/move?limit=1000'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return [move['name'] for move in data['results']]
    else:
        raise Exception('Failed to fetch move list')

