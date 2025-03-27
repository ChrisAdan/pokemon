{{ config(
    materialized='view',
    persist_docs={'relation': true, 'columns': true}
)}}

select
    -- Basic descriptive information
    id,
    raw_response:num::int as number,
    name,
    raw_response:types[0].name::varchar(100) as primary_type,
    raw_response:types[1].name::varchar(100) as secondary_type,
    -- Base stats
    raw_response:baseStatsTotal::int as base_stats_total,
    raw_response:baseStats.hp::int as hp,
    raw_response:baseStats.attack::int as attack,
    raw_response:baseStats.specialattack::int as special_attack,
    raw_response:baseStats.defense::int as defense,
    raw_response:baseStats.specialdefense::int as specialdefense,
    raw_response:baseStats.speed::int as speed,
    -- Gender distribution
    {{ convert_percent_string_to_number('raw_response:gender.male') }} as percent_male,
    {{ convert_percent_string_to_number('raw_response:gender.female') }} as percent_female,
    -- Physical characteristics
    raw_response:height::number(5, 2) as height,
    raw_response:weight::number(5, 2) as weight,
    raw_response:levellingRate::varchar(255) as leveling_rate,
    -- Egg context
    raw_response:isEggObtainable::boolean as is_egg_obtainable,
    raw_response:minimumHatchTime::int as min_hatch_time,
    raw_response:maximumHatchTime::int as max_hatch_time,
    -- Special status
    raw_response:legendary::boolean as is_legendary,
    raw_response:mythical::boolean as is_mythical,
    -- EV yields
    raw_response:evYields.hp::int as ev_yield_hp,
    raw_response:evYields.attack::int as ev_yield_attack,
    raw_response:evYields.specialattack::int as ev_yield_sp_attack,
    raw_response:evYields.defense::int as ev_yield_defense,
    raw_response:evYields.specialdefense::int as ev_yield_sp_def,
    raw_response:evYields.speed::int as ev_yield_speed
from pokemon_db.raw.pokemon_raw


