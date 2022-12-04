#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_city import City

if __name__ == "__main__":
    """ This is the code implem"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    states_inst = session.query(State, City)\
    .filter(City.state_id == State.id).all()
    for state, city in states_inst:
        print('{0}: ({1}) {2}'.format(state.name, city.id, city.name))
