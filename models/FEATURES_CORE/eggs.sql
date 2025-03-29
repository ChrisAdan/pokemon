{{ config(
    materialized='view',
    persist_docs={'relation': True, 'columns': True}) }}

select
    id,
    percent_male,
    percent_female,
    is_egg_obtainable,
    min_hatch_time,
    max_hatch_time
from {{ ref('pokemon_stage') }}