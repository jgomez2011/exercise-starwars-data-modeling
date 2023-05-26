import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__="users"
    id = Column(Integer, primary_key = True)
    username = Column(String(27), nullable = False, unique = True)
    password = Column(String(24), nullable = False,)
    email = Column(String(52), nullable = False, unique = True)

class Characters(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key = True)
    name = Column(String(33), nullable = False, default = "unknown")
    height = Column(String(10), nullable = False, default = "n/a")
    race = Column(String(19), nullable = False, default = "n/a")
    origin_planet = Column(String(23), nullable = False, default = "n/a")

class Planets(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = False, default = "unknown")
    terrain = Column(String(20), nullable = False, default = "unexplored")
    climate = Column(String(19), nullable = False, default = "unexplored")
    population = Column(Integer, nullable = False, default = "unexplored")

class Favorites(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key = True)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable = True)
    character = relationship(Characters)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable = True)
    planet = relationship(Planets)
    user_id = Column(Integer, ForeignKey('users.id'), nullable = False)
    user = relationship(Users)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
