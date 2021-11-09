#!/usr/bin/python3
""" script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa """
if __name__ == "__main__":
    import sys
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{\
}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker()
    session = session(bind=engine)
    state = session.query(State).filter(State.name.contains('a'))
    for hell in state:
        print("{}: {}".format(hell.id, hell.name))
