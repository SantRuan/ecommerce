import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
db_params = {
    'host': 'postgres_db',
    'port': '5432',
    'user': 'postgres',
    'password': 'postgres123',
    'database': 'postgres'
}


def create_database():
    connection = psycopg2.connect(**db_params)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    db_name = 'ecommerce_db'

    cursor = connection.cursor()
    cursor.execute(
        sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), (db_name,))
    exists = cursor.fetchone()

    if not exists:
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(
            sql.Identifier(db_name))
        )


if __name__ == "__main__":
    create_database()
