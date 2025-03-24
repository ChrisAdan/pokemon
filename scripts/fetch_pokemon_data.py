import requests
import json

url = 'https://graphqlpokemon.favware.tech/v8'

headers = {
    'Content-Type':'application/json',
}

def dispatch(response):
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("API call failed with status code " + str(response.status_code))

def fetch_single_pokemon(name='dragonite'):
    '''Pass string with Pokemon name to call getPokemon(). Return response.json().
    Default: dragonite'''
    with open(f'../queries/extract_single_pokemon.gql', 'r') as file:
        query = ''.join(line for line in file if not line.strip().startswith('#'))

    variables= {
        'pokemon': name,
    }

    response = requests.post(url, json={'query':query, 'variables':variables}, headers=headers)
    dispatch(response)

def fetch_all_pokemon(include_special=False):
    '''Fetch a list by calling getAllPokemon(). Return response.json().
    Optional parameter: include_special (default: False)'''
    with open(f'../queries/extract_pokemon.gql', 'r') as file:
        query = ''.join(line for line in file if not line.strip().startswith('#'))
    if not include_special:
        variables= {
            'offset':89
        }
    response = requests.post(url, json={'query':query, 'variables':variables if variables else None}, headers=headers)
    dispatch(response)

def fetch_single_move(name='absorb'):
    '''Pass string with Move name to call getMove(). Return response.json().
    Default: absorb'''
    with open(f'../queries/extract_single_move.gql', 'r') as file:
        query = ''.join(line for line in file if not line.strip().startswith('#'))

    variables= {
        'move':name
    }
    response = requests.post(url, json={'query':query, 'variables':variables}, headers=headers)
    dispatch(response)

def fetch_single_nature(name='jolly'):
    '''Pass string with Nature name to call getNature(). Return response.json().
    Default: jolly'''
    with open(f'../queries/extract_single_nature.gql', 'r') as file:
        query = ''.join(line for line in file if not line.strip().startswith('#'))

    variables= {
        'nature':name
    }
    response = requests.post(url, json={'query':query, 'variables':variables}, headers=headers)
    dispatch(response)

def fetch_all_natures():
    '''Fetch a list by calling getAllNatures(). Return response.json().'''
    with open(f'../queries/extract_natures.gql', 'r') as file:
        query = ''.join(line for line in file if not line.strip().startswith('#'))

    response = requests.post(url, json={'query':query}, headers=headers)
    dispatch(response)

def fetch_type_matchup(primary_type='fire', secondary_type='ghost'):
    '''Pass a string primary_type and secondary_type to call getTypeMatchup(). Return response.json().
    Defaults:
        primary_type: fire
        secondary_type: ghost'''
    with open(f'../queries/extract_types.gql', 'r') as file:
        query = ''.join(line for line in file if not line.strip().startswith('#'))  
        variables = {
        'primaryType': primary_type.lower(),
        'secondaryType': secondary_type.lower()
        }
        response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)
        dispatch(response)


