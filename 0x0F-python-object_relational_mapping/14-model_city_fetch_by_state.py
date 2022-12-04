#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states_inst = session.query(City, State)
    .filter(City.state_id == State.id).order_by(cities.id).all()
    for state, city in states_inst:
        print('{0}: ({1}) {2}'.format(state.name, city.id, city.name))
