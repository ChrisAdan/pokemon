{{ config(materialized='view')}}

select
    id,
    primary_type,
    secondary_type,
    relation_type,
    related_type
    from {{ ref('clf_primary_type_core_split_full')}}
where split = 'train'