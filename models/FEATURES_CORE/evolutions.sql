{{ config(
    materialized='view',
    persist_docs={'relation': True, 'columns': True}) }}

select
    id,
    leveling_rate,
    is_legendary,
    is_mythical
from {{ ref('pokemon_stage')}}