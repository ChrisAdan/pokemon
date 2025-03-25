import snowflake.connector
from dotenv import load_dotenv
import datetime
import os
import json

tables = {
    'pokemon':'POKEMON_RAW',
    'natures':'NATURES_RAW',
    'moves':'MOVES_RAW',
    'types':'TYPES_RAW'
}

load_dotenv()

def connect_to_snowflake():
    conn = snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
        database=os.getenv('SNOWFLAKE_DATABASE'),
        schema=os.getenv('SNOWFLAKE_SCHEMA')
    )

    cursor = conn.cursor()
    return conn, cursor

def load_to_snowflake(data, schema):
    """
    Inserts a record into the appropriate raw table in Snowflake.

    Args:
        schema (str): The schema key to retrieve the correct table name.
        data (dict): The data to load into Snowflake. Raw API response.
    """
    print(f'Data Received of type {type(data)}:')
    print(data)
    if schema not in tables:
        raise ValueError(f"Invalid schema key: {schema}.")

    table_name = tables[schema]  # Retrieve the correct table name

    conn, cursor = connect_to_snowflake()

    if not isinstance(data, dict):
        raise ValueError(f"Unexpected data format in {data}")

    record_id = hash(data['key']) % (10 ** 20)
    name = data.get('key', 'Unknown')
    created_at = datetime.datetime.now(datetime.timezone.utc)
    raw_response = json.dumps(data)

    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        ID NUMBER(20,0) COMMENT 'Primary Key. Unique identifier for the record.',
        NAME VARCHAR(255) COMMENT 'The record''s name.',
        RAW_RESPONSE VARIANT COMMENT 'The full API response stored in JSON format.',
        CREATED_AT TIMESTAMP_LTZ(9) COMMENT 'Timestamp when the record was ingested.'
    );"""

    insert_query = f'''
    insert into {table_name} (ID, NAME, RAW_RESPONSE, CREATED_AT)
    Values (%s, %s, parse_json(%s), %s);'''
    
    cursor.execute(insert_query, (record_id, name, raw_response, created_at))

    conn.commit()
    cursor.close()
    conn.close()

    print(f"Inserted record into {table_name}. ID: {record_id} | Name: {name}")



    

    