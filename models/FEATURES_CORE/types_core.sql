{{ config(
    materialized='view',
    persist_docs={'relation': True, 'columns': True}) }}

select
    id,
    primary_type,
    secondary_type,
    relation_type,
    related_type
from {{ ref('types_stage')}}