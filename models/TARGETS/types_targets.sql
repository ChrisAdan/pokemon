{{ config(
    materialized='view',
    persist_docs={'relation': True, 'columns': True}) }}

with relations as (
    select 
        distinct relation_type
    from {{ ref('types_stage')}}
)

select
    id,
    primary_type,
    secondary_type,
    {% for relation in relations %}
        MAX(CASE WHEN relation_type = '{{ relation }}' THEN related_type END) 
            AS {{ relation }}{% if not loop.last %}, {% endif %}
    {% endfor %}
from {{ ref('types_stage') }}
group by 1, 2, 3
        