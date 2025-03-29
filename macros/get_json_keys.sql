{% macro get_json_keys(table_name, column_name) %}
    {% if execute %}
        {% set query %}
            select
                distinct key
            from {{ table_name }},
            lateral flatten(input => {{ column_name }})
        {% endset %}

        {% set results = run_query(query) %}
        
        {# Log the results object to see the full structure #}
        {% do log('Query results: ' ~ results, info=True) %}

        {% set keys = results.columns[0].values() %}
        
        {# Log the values of the keys array #}
        {% do log('Keys: ' ~ keys, info=True) %}
    {% else %}
        {% set keys = [] %}
    {% endif %}

    {% do return(keys) %}
{% endmacro %}