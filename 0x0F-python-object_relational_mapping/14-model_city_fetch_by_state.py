#!/usr/bin/python3
"""
 Lists all states via SQLAlchemy
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_city import City, State, Base


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State.name, City.id, City.name).\
        filter(City.state_id == State.id).order_by(City.id)
    for r in results:
        print("{}: ({}) {}".format(r[0], r[1], r[2]))
    session.close()
