{% macro add_column_comments() %}
  {% for model in dbt.models %}
    {% if model.columns is defined %}
      {% for column in model.columns %}
        {% if column.description is not none %}
          {% set description = column.description | replace("'", "''") %}
          {% set column_name = model.schema ~ '.' ~ model.name ~ '.' ~ column.name %}
          
          -- Log the column and description to dbt logs
          {% do log('Applying comment for column: ' ~ column_name ~ ' with description: ' ~ description, info) %}
          
          -- Apply the comment to Snowflake
          EXECUTE IMMEDIATE 
            'COMMENT ON COLUMN ' || column_name || ' IS ''' || description || '''';
        {% else %}
          {% do log('No description for column: ' ~ column.name, info) %}
        {% endif %}
      {% endfor %}
    {% endif %}
  {% endfor %}
{% endmacro %}
