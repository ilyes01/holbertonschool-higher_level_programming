#!/usr/bin/python3
"""script that lists all City objects from the database hbtn_0e_101_usa"""
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State, City
    user = argv[1]
    pwd = argv[2]
    dbname = argv[3]
    connection = "mysql+mysqldb://{}:{}@localhost:3306/{}".\
                 format(user, pwd, dbname)
    engine = create_engine(connection, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City).join(City.state).\
        order_by(City.id).all()
    for city in query:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
