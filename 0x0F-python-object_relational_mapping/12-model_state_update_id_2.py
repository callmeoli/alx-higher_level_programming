#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sqlalchemy import update

if __name__ == "__main__":
    """ prints a conatining seletions"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    if stateUpdated:
        stateUpdated = session.query(State).filter(State.id == 2).first()
        upd = update(State)
        val = upd.values({State.name: "New Mexico"})
        cond = val.where(State.c.id == 2)
