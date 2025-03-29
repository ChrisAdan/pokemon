{{ config(
    materialized='view',
    persist_docs={'relation': True, 'columns': True}) }}

{% set relations = [
    'attacking_double_effective',
    'attacking_effective',
    'attacking_resisted',
    'attacking_effectless',
    'attacking_normal',
    'defending_double_effective',
    'defending_effective',
    'defending_resisted',
    'defending_effectless',
    'defending_normal',
    'defending_double_resisted'
] %}

with source as (
    select
        id, 
        raw_response:primary_type::varchar(50) as primary_type,
        raw_response:secondary_type::varchar(50) as secondary_type,
        raw_response as raw_json        
    from pokemon_db.raw.types_raw
)

{% for relation in relations %}
    SELECT
        id,
        primary_type,
        secondary_type,
        '{{ relation }}' AS relation_type,
        f.value::STRING AS related_type
    FROM source,
    LATERAL FLATTEN(input => raw_json:{{ relation }}) AS f
    {% if not loop.last %}
    UNION ALL
    {% endif %}
    {% endfor %}