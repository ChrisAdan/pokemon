{% macro train_test_split(source_relation, target_column, partitions = 5, split_ratio=0.8) %}
with base as (
    select *, 
           ntile({{ partitions|int }}) over (partition by {{ target_column }} order by random()) as split_bucket
    from {{ source_relation }}
),
splits as (
    select *, 
           case 
               when split_bucket <= {{ (split_ratio * partitions) | round(0, 'floor') | int }} then 'train'
               else 'test'
           end as split
    from base
)
select * from splits
{% endmacro %}
