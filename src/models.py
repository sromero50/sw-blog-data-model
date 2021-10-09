import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    userName = Column(String(150))
    password = Column(String(150))
    

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    gender = Column(String(150), nullable=False)
    hair_color = Column(String(150), nullable=False)
    eye_color = Column(String(150),  nullable=False)


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String(150), nullable=False)


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    vehicle_class = Column(String(150), nullable=False)
    manufacturer = Column(String(150), nullable=False)

class FavoritePlanet(Base):
    __tablename__ = 'favoritePlanet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user = relationship(User)
    planet = relationship(Planet)

class FavoriteVehicle(Base):
    __tablename__ = 'favoriteVehicle'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    user = relationship(User)
    vehicle = relationship(Vehicle)

class FavoriteCharacter(Base):
    __tablename__ = 'favoriteCharacter'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    user = relationship(User)
    character = relationship(Character)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')