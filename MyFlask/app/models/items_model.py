from sqlalchemy.orm import relationship
from app.database import db

class Item(db.Model):
    __tablename__ = 'FoodItems'  # Matches the exact table name in your database

    item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    price = db.Column(db.DECIMAL(10, 2), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('Categories.cat_id'), nullable=False)  # Matches the exact column name in Categories

    # Optional relationships (commented out as per your provided model)
    # category = relationship('Category', back_populates='items')
    # order_items = relationship('OrderItem', back_populates='items')
