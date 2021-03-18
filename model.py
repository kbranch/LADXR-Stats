from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    area = Column(String)

    def __init__(self, name, description, area):
        self.name = name
        self.description = description
        self.area = area

class Rom(Base):
    __tablename__ = 'rom'

    id = Column(Integer, primary_key=True)
    seed = Column(String)

    def __init__(self, seed):
        self.seed = seed

class Flag(Base):
    __tablename__ = 'flag'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(String)

    romId = Column(Integer, ForeignKey('rom.id'))
    rom = relationship("Rom", back_populates="flags")

    def __init__(self, name, value, rom):
        self.name = name
        self.value = value
        self.rom = rom

class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    sphere = Column(Integer)
    player = Column(Integer)

    locationId = Column(Integer, ForeignKey('location.id'))
    location = relationship("Location")

    romId = Column(Integer, ForeignKey('rom.id'))
    rom = relationship("Rom", back_populates='items')

    def __init__(self, name, sphere, player, location, rom):
        self.name = name
        self.sphere = sphere
        self.player = player
        self.location = location
        self.rom = rom

Rom.flags = relationship("Flag", order_by=Flag.id, back_populates='rom')
Rom.items = relationship("Item", order_by=Item.id, back_populates='rom')