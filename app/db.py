import os
from typing import Union
import psycopg2


def get_db_conn() -> Union[psycopg2.extensions.connection, None]:
    try:
        conn = psycopg2.connect(
            dbaname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
        )
        return conn
    except psycopg2.Error as e:
        print(e)
    return None


def get_cursor(
    conn: psycopg2.extensions.connection,
) -> Union[psycopg2.extensions.cursor, None]:
    try:
        cur = conn.cursor()
        return cur
    except psycopg2.Error as e:
        print(e)

    return None
