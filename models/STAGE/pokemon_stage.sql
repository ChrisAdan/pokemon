{{ config(
    materialized='view',
    persist_docs={'relation': true, 'columns': true}
)}}

select
    -- Basic descriptive information
    id,
    raw_response:num::int as number comment 'The Pokemon''s local PokeDex number (duplicates between generations)',
    name,
    -- Base stats
    raw_response:baseStatsTotal::int as base_stats_total comment 'Sum of Pokemon Base Stats',
    raw_response:baseStats.hp::int as hp comment 'Base HP',
    raw_response:baseStats.attack::int as attack comment 'Base Attack stat',
    raw_response:baseStats.specialattack::int as special_attack comment 'Base Sp. Attack stat',
    raw_response:baseStats.defense::int as defense comment 'Base Defense stat',
    raw_response:baseStats.specialdefense::int as specialdefense comment 'Base Sp. Defense stat',
    raw_response:baseStats.speed::int as speed comment 'Base Speed stat',
    -- Gender distribution
    raw_response:gender.male::number(5, 2) as percent_male comment 'Percentage of Pokemon that are Male',
    raw_response:gender.female::number(5, 2) as percent_female comment 'Percentage of Pokemon that are Female',
    -- Physical characteristics
    raw_response:height::number(5, 2) as height comment 'Pokemon Height in meters',
    raw_response:weight::number(5, 2) as weight comment 'Pokemon Weight in meters',
    raw_response:evolutionLevel::int as evolution_level comment 'Pokemon''s evolution level, if applicable',
    raw_response:levellingRate::varchar(255) as leveling_rate comment 'The leveling rate of the Pokemon',
    -- Egg context
    raw_response:isEggObtainable::boolean as is_egg_obtainable comment 'Is Pokemon obtainable from egg',
    raw_response:minimumHatchTime::int as min_hatch_time comment 'The minimum egg hatch time',
    raw_response:maximumHatchTime::int as max_hatch_time comment 'The maximum egg hatch time',
    -- Special status
    raw_response:legendary::boolean as is_legendary comment 'Is Pokemon legendary',
    raw_response:mythical::boolean as is_mythical comment 'Is Pokemon mythical',
    -- EV yields
    raw_response:evYields.hp::int as ev_yield_hp comment 'HP EV Yield',
    raw_response:evYields.attack::int as ev_yield_attack comment 'Attack EV Yield',
    raw_response:evYields.specialattack::int as ev_yield_sp_attack comment 'Sp. Attack EV Yield',
    raw_response:evYields.defense::int as ev_yield_defense comment 'Defense EV Yield',
    raw_response:evYields.specialdefense::int as ev_yield_sp_def comment 'Sp. Defense EV Yield',
    raw_response:evYields.speed::int as ev_yield_speed comment 'Speed EV Yield'
from {{ ref('pokemon_raw') }}


