import os


def get_postgres_uri():
    host = os.environ.get("DB_HOST", "postgres_db")
    port = 5432
    password = os.environ.get("DB_PASSWORD", "postgres123")
    user, db_name = "postgres", "ecommerce_db"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
