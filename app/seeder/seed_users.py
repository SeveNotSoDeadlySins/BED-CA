from app.db.db import SessionLocal, Users, Base, engine
from passlib.context import CryptContext

# Create tables if the table doesnt exist
Base.metadata.create_all(bind=engine)

# Hasing a password useing passlib and bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain_password: str) -> str:
    truncated = plain_password[:12]  # only first 12 chars
    return pwd_context.hash(truncated)

db = SessionLocal()

print("Starting seed script...")

# Data for seeding. Raw data
raw_users = [
    {'name': 'John Cena', 'email': 'johncena@example.com', 'password': 'password123'},
    {'name': 'Jane Smith', 'email': 'janesmith@example.com', 'password': 'password456'},
]

if db.query(Users).count() == 0:
    print("Table empty, adding users...")
else:
    print("Users table already has data")

# Insert the data if the table is empty
if db.query(Users).count() == 0:
    users_to_add = []
    for i in raw_users:
        # hashes the password before storing it in the database
        hashed = hash_password(i['password'])
        user = Users(name=i['name'], email=i['email'], password=hashed)
        users_to_add.append(user)

    db.add_all(users_to_add)
    db.commit()
    print('Users added to table')
else:
    print('Data on table already exists')

db.close()