from app.database.database import SessionLocal

def check_database_connection():
    print("🚀 check_db.py started")
    try:
        session = SessionLocal()

        engine = session.get_bind()
        db_name = engine.url.database

        print("Database: ", db_name)
        session.close()
    except Exception as e :
        print("Database connection failed")
        print("Error:",e)
 
check_database_connection()