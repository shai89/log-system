from dotenv import load_dotenv
load_dotenv()

from db.base import Base
from models.log_db_model import Log
from db.session import engine

def create_tables():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print(" Done.")

if __name__ == "__main__":
    create_tables()
