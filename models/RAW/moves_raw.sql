{{ config(materialized='table', persist_docs={'relation': true, 'columns': true}) }}

SELECT 
    CAST(NULL AS NUMBER(20,0)) AS id,            -- Unique identifier for the Move
    CAST(NULL AS VARCHAR(255)) AS name,          -- The Move's name
    CAST(NULL AS VARIANT) AS raw_response,       -- Full API response in JSON format
    CURRENT_TIMESTAMP AS created_at             -- Timestamp when the record was ingested
