import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password= Column(String(20), nullable=False)
    email=Column(String(30), nullable=False)
    # favoritos_id = Column(Integer, ForeignKey('favoritos.id'))
    # favoritos = relationship(Favoritos)

class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    genero = Column(String(250), nullable=False)
    color_piel = Column(String(250), nullable=False)
    color_pelo = Column(String(250), nullable=False)
    color_ojos = Column(String(250), nullable=False)
    fecha_nacimiento = Column(String(250), nullable=False)
    # favoritos_id = Column(Integer, ForeignKey('favoritos.id'))
    # favoritos = relationship(Favoritos)
class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    agregar = Column(String(250), nullable=False)
    eliminar = Column(String(250), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)
    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    planetas = relationship(Usuario)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(Usuario)
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    personajes = relationship(Usuario)

class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    poblacion = Column(String(250))
    terreno = Column(String(250))
    # favoritos_id = Column(Integer, ForeignKey('favoritos.id'))
    # favoritos = relationship(Favoritos)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    modelo = Column(String(250))
    año_creacion= Column(String(250))
    capacidad = Column(String(250), nullable=False)
    # favoritos_id = Column(Integer, ForeignKey('favoritos.id'))
    # favoritos = relationship(Favoritos)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
