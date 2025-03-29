{{ config(
    materialized='view',
    persist_docs={'relation': True, 'columns': True}) }}

select
    id,
    increased_stat,
    decreased_stat,
    preferred_flavor,
    disliked_flavor
from {{ ref('natures_stage')}}