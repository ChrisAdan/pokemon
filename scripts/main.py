import concurrent.futures
import json
import fetch_pokemon_data as fpd
import transform as tr
import load_to_snowflake as ld
import sys

schemas = ld.tables.keys()

class DataProcessor:
    def __init__(self, schema):
        self.schema = schema
    
    def process_schema(self):
        '''Fetch, transform (if needed), and load data for a given schema'''
        if self.schema == 'moves':
            self.process_moves()
        elif self.schema in ['pokemon', 'natures']:
            self.fetch_and_load()
        elif self.schema == 'types':
            self.process_types()

    def process_moves(self):
        '''Fetch, transform, and load move data using ThreadPoolExecutor'''
        move_names = fpd.fetch_all_moves()
        if not move_names:
            print('Failed to retrieve move list')
            return
        move_names = [tr.standardize_move_name(move) for move in move_names]
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            future_to_move = {executor.submit(fpd.fetch_single_move, move): move for move in move_names}
            
            for future in concurrent.futures.as_completed(future_to_move):
                move_name = future_to_move[future]
                print(f'Current move: {move_name}')
                try:
                    data = future.result()
                    if data:
                        ld.load_to_snowflake(data, schema)
                except Exception as e:
                    print(e)
                    sys.exit(f'Error processing {move_name}')

    def fetch_and_load(self):
        '''Fetch data for getAll queries, then load into Snowflake'''
        method_name = f'fetch_all_{schema}'

        if hasattr(fpd, method_name):
            method = getattr(fpd, method_name)
            data = method()
            for pokemon in data:
                ld.load_to_snowflake(pokemon, schema)
        else:
            print(f'Method {method_name} not found in fetch_pokemon_data')
    
    def process_types(self):
        '''Fetch, transform, and load Type matchup data'''
        types = [
            'Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 
            'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 
            'Steel', 'Fairy'
        ]
        if hasattr(fpd, 'fetch_type_matchup'):
            for primary_type in types:
                for secondary_type in types:
                    if primary_type == secondary_type:
                        continue
                    data = tr(fpd.fetch_type_matchup(primary_type, secondary_type))
                    data['primary_type'] = primary_type
                    data['secondary_type'] = secondary_type
                    ld.load_to_snowflake(data, schema)
        else:
            print('Method fetch_type_matchup not found in fetch_pokemon_data')

if __name__ == '__main__':
    for schema in schemas:
        # DONE: Pokemon
        # TODO: Natures, Types
        # CURRENT: Moves
        if schema not in ['pokemon', 'natures', 'types']:
            print(f'Beginning {schema}')
            processor = DataProcessor(schema)
            processor.process_schema()