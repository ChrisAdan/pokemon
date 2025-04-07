{% macro train_test_split(features_cte, targets_cte, partitions=5, split_ratio=0.8) %}
with features as (
    {{ features_cte }}
),
targets as (
    {{ targets_cte }}
),
joined as (
    select f.*, t.*
    from features f
    join targets t on f.id = t.id
),
base as (
    select *, 
           ntile({{ partitions|int }}) over (partition by t.{{ target_column }} order by random()) as split_bucket
    from joined
),
splits as (
    select *, 
           case 
               when split_bucket <= {{ (split_ratio * partitions)|round(0, 'floor')|int }} then 'train'
               else 'test'
           end as split
    from base
)
select * from splits
{% endmacro %}
