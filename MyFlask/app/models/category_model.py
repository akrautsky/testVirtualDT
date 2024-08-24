from sqlalchemy.orm import relationship
from app.database import db

class Category(db.Model):
    __tablename__ = 'Categories'

    cat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

    # Define the relationship to the Item model
    # items = relationship('Item', back_populates='category')
