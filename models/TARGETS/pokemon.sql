{{ config(
    materialized='view',
    persist_docs={'relation': True, 'columns': True}) }}

select
    id,
    primary_type,
    secondary_type,
    leveling_rate,
    is_egg_obtainable,
    is_legendary,
    is_mythical
from {{ ref('pokemon_stage')}}