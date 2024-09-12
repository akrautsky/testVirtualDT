from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

# Base declarative class
Base = declarative_base()

# Categories table
class Category(Base):
    __tablename__ = 'Categories'

    cat_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)

    # Relationship to Items (one category can have many items)
    items = relationship('Item', back_populates='category')

# Items table
class Item(Base):
    __tablename__ = 'Items'

    item_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    price = Column(DECIMAL(10, 2), nullable=False)
    category_id = Column(Integer, ForeignKey('Categories.cat_id'), nullable=True)

    # Relationship to Categories (many items belong to one category)
    category = relationship('Category', back_populates='items')
    order_items = relationship('OrderItem', back_populates='item')

# Orders table
class Order(Base):
    __tablename__ = 'Orders'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(DateTime, default=datetime.utcnow)
    order_total = Column(DECIMAL(10, 2), nullable=False)
    total_items = Column(Integer, nullable=False)
    tip_amount = Column(DECIMAL(10, 2), default=0.00)
    roundedDollar = Column(DECIMAL(10, 2), default=0.00, nullable=False)

    # Relationship to OrderItems (one order can have many order items)
    order_items = relationship('OrderItem', back_populates='order')

# OrderItems table
class OrderItem(Base):
    __tablename__ = 'OrderItems'

    order_item_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('Orders.order_id'), nullable=False)
    item_id = Column(Integer, ForeignKey('Items.item_id'), nullable=False)
    quantity = Column(Integer, nullable=False)

    # Relationships to Orders and Items
    order = relationship('Order', back_populates='order_items')
    item = relationship('Item', back_populates='order_items')
