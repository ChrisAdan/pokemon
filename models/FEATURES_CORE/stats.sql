{{ config(
    materialized='view',
    persist_docs={'relation': True, 'columns': True}) }}

select
    id,
    height,
    weight,
    base_stats_total,
    hp,
    attack,
    special_attack,
    defense,
    special_defense,
    speed,
    ev_yield_hp,
    ev_yield_attack,
    ev_yield_sp_attack,
    ev_yield_defense,
    ev_yield_sp_def,
    ev_yield_speed
from {{ ref('pokemon_stage')}}