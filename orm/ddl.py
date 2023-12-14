import random
from .dml import User

import sqlalchemy
from dotenv import load_dotenv
import os
import sqlalchemy.orm
from geoalchemy2 import Geometry
from faker import Faker

load_dotenv()

# tworze plik o nazwie .env

db_params = sqlalchemy.URL.create(
    drivername='postgresql+psycopg2',
    username=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('POSTGRES_HOST'),
    database=os.getenv('POSTGRES_DB'),
    port=os.getenv('POSTGRES_PORT'),

)
engine = sqlalchemy.create_engine(db_params)
connection = engine.connect()


Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()
## Create /insert
lista_userow: list = []
fake = Faker()

for item in range(10_000):
    lista_userow.append(
        User(
            name=fake.name(),
            location=f'POINT({random.uniform(14,24)} {random.uniform(49,55)})'
        )
    )

#Read / select


users_from_db = session.query(User).all()



session.commit()

# user_from_db = session.query(User).filter(User.name=='Catherine Ibarra')


# session.add_all(lista_userow)
# session.commit()

session.flush()
connection.close()
engine.dispose()

def manin():
    load_dotenv()

    # tworze plik o nazwie .env

    db_params = sqlalchemy.URL.create(
        drivername='postgresql+psycopg2',
        username=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('POSTGRES_HOST'),
        database=os.getenv('POSTGRES_DB'),
        port=os.getenv('POSTGRES_PORT'),

    )
    engine = sqlalchemy.create_engine(db_params)
    connection = engine.connect()

    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()
    ## Create /insert
    lista_userow: list = []
    fake = Faker()

    for item in range(10_000):
        lista_userow.append(
            User(
                name=fake.name(),
                location=f'POINT({random.uniform(14, 24)} {random.uniform(49, 55)})'
            )
        )

    # Read / select

    users_from_db = session.query(User).all()

    session.commit()

    # user_from_db = session.query(User).filter(User.name=='Catherine Ibarra')

    # session.add_all(lista_userow)
    # session.commit()

    session.flush()
    connection.close()
    engine.dispose()


if __name__ == __main__:
    main()