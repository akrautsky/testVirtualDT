from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

# Initialize the database connection
engine = create_engine('mysql+pymysql://root:Akashr%4007@localhost:3306/VDOrderDB')

# Initialize the metadata object for reflection
metadata = MetaData()

# Base declarative class
Base = declarative_base(metadata=metadata)

# Reflect the tables
class Order(Base):
    __tablename__ = 'Orders'
    __table_args__ = {'autoload_with': engine}

class Category(Base):
    __tablename__ = 'Categories'
    __table_args__ = {'autoload_with': engine}

class Item(Base):
    __tablename__ = 'Items'
    __table_args__ = {'autoload_with': engine}

class OrderItem(Base):
    __tablename__ = 'OrderItems'
    __table_args__ = {'autoload_with': engine}

class FoodItem(Base):
    __tablename__ = 'FoodItems'
    __table_args__ = {'autoload_with': engine}
