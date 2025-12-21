from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:password@localhost:5432/testdb"

engine = create_engine(DATABASE_URL)

def check_db_connection():
    try:
        with engine.connect() as conn:
            return "Postgres Connected Successfully"
    except Exception as e:
        return str(e)
