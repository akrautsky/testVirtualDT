from datetime import datetime
from sqlalchemy.orm import relationship
from app.database import db

class Order(db.Model):
    __tablename__ = 'Orders'
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_total = db.Column(db.DECIMAL(10,2), nullable=False)
    order_date = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    total_items = db.Column(db.Integer, nullable=False)
    tip_amount = db.Column(db.DECIMAL(10,2), default=0.0)
    roundedDollar = db.Column(db.DECIMAL(10,2), nullable=False, default=0.0)

    # Define the relationship to the OrderItem model
    # order_items = relationship("OrderItem", back_populates="orders")
