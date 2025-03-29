{{ config(
    materialized='view',
    persist_docs={'relation': True, 'columns': True}) }}

select
    id,
    raw_response:name::varchar(100) as name,
    raw_response:key::varchar(100) as key,
    raw_response:category::varchar(100) as category,
    raw_response:type::varchar(100) as type,
    raw_response:target::varchar(100) as target,
    raw_response:pp::int as pp,
    raw_response:accuracy::int as accuracy,
    raw_response:basePower::varchar(255) as base_power_str,
    raw_response:maxMovePower::int as max_move_power,
    raw_response:zMovePower::int as z_move_power,
    raw_response:priority::int as priority,
    raw_response:contestType::varchar(100) as contest_type
from pokemon_db.raw.moves_raw
