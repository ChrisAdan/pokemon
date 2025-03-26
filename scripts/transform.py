def transform_matchup_data(raw_data):
    '''Function to unpack Type matchup API response. Unpacks attacking and defending
    properties and nested effectiveness data.
    Arguments:
        raw_data: API response dict for single Type matchup
    Returns: transformed_data objects'''
      
    attacking = raw_data['attacking']
    defending = raw_data['defending']
    
    transformed_data = {
        'attacking_double_effective': attacking['doubleEffectiveTypes'],
        'attacking_double_resisted': attacking['doubleResistedTypes'],
        'attacking_effective': attacking['effectiveTypes'],
        'attacking_effectless': attacking['effectlessTypes'],
        'attacking_normal': attacking['normalTypes'],
        'attacking_resisted': attacking['resistedTypes'],
        
        'defending_double_effective': defending['doubleEffectiveTypes'],
        'defending_double_resisted': defending['doubleResistedTypes'],
        'defending_effective': defending['effectiveTypes'],
        'defending_effectless': defending['effectlessTypes'],
        'defending_normal': defending['normalTypes'],
        'defending_resisted': defending['resistedTypes'],
    }
    return transformed_data


def standardize_move_name(raw_moves):
    edge_map = {
        'vice-grip': 'visegrip',
    }
    output = []
    for move_name in raw_moves:
        if move_name in edge_map.keys():
            output.append(edge_map[move_name])
        else:
            output.append(move_name.replace('-', ''))
    return output