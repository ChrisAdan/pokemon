{{ config(materialized='view') }}

{{ train_test_split('pokemon_db.dbt_features_core.types_core', 'primary_type') }}
