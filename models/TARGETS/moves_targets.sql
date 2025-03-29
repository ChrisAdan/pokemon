{{ config(
    materialized='view',
    persist_docs={'relation': True, 'columns': True}) }}

select
    id,
    category,
    type,
    target,
    contest_type
from {{ ref('moves_stage')}}