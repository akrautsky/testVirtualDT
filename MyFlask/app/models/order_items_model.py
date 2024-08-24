from sqlalchemy import CheckConstraint
from sqlalchemy.orm import relationship
from app.database import db

class OrderItem(db.Model):
    __tablename__ = 'OrderItems'  # Matches the exact table name in your database

    order_item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('Orders.order_id'), nullable=False)  # Matches the exact column name in Orders
    item_id = db.Column(db.Integer, db.ForeignKey('FoodItems.item_id'),nullable=False)  # , db.ForeignKey('Items.item_id') Matches the exact column name in Items db.ForeignKey('Items.item_id'), 
    quantity = db.Column(db.Integer, nullable=False)

    # Optional relationships (commented out as per your provided model)
    # orders = relationship("Order", back_populates="order_items")
    # items = relationship("Item", back_populates="order_items")

    # Adding the check constraint for quantity > 0
    __table_args__ = (
        CheckConstraint('quantity > 0', name='quantity_positive'),
    )
