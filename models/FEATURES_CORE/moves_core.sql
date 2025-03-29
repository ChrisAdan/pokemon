{{ config(
    materialized='view',
    persist_docs={'relation': True, 'columns': True}) }}

select
    id,
    category,
    type,
    target,
    pp,
    accuracy,
    max_move_power,
    z_move_power,
    priority,
    contest_type
from {{ ref('moves_stage')}}