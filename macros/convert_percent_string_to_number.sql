{% macro convert_percent_string_to_number(percentage_str) %}
    cast(replace({{ percentage_str }}, '%', '') as number(5, 2))
{% endmacro %}