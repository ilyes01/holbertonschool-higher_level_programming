#!/usr/bin/python3
""" script
"""
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    user = argv[1]
    pwd = argv[2]
    dbname = argv[3]
    connection = "mysql+mysqldb://{}:{}@localhost:3306/{}".\
                 format(user, pwd, dbname)
    engine = create_engine(connection, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter(State.name.like('%a%')).all()
    for row in query:
        print("{}: {}".format(row.id, row.name))
