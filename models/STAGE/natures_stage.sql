{{ config(
    materialized='view',
    persist_docs={'relation': true, 'columns': true}
)}}

select
       id,
       name,
       raw_response:increasedStat::varchar(100) increased_stat,
       raw_response:decreasedStat::varchar(100) decreased_stat,
       raw_response:preferredFlavor::varchar(100) preferred_flavor,
       raw_response:dislikedFlavor::varchar(100) disliked_flavor
from pokemon_db.raw.natures_raw


