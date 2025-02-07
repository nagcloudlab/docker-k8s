from flask import Flask, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base
import os

app = Flask(__name__)

# Get PostgreSQL URI from environment variable
POSTGRES_URI = os.getenv('POSTGRES_URI', 'default-url')


# Initialize SQLAlchemy
engine = create_engine(POSTGRES_URI)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    comment = Column(String)
    rating = Column(Float)

Base.metadata.create_all(engine)
session = Session()

@app.route('/review/<int:product_id>', methods=['GET'])
def get_reviews(product_id):
    reviews = session.query(Review).filter(Review.product_id == product_id).all()
    reviews_list = [{"id": r.id, "comment": r.comment, "rating": r.rating} for r in reviews]
    return jsonify(reviews_list), 200

if __name__ == '__main__':
    # Pre-populate with sample data if table is empty
    if session.query(Review).count() == 0:
        sample_reviews = [
            Review(product_id=1, comment="Excellent product!", rating=5),
            Review(product_id=1, comment="Good value for money.", rating=4),
            Review(product_id=2, comment="Not what I expected.", rating=2),
            Review(product_id=2, comment="Could be better.", rating=3)
        ]
        session.add_all(sample_reviews)
        session.commit()
    app.run(host='0.0.0.0', port=5003, debug=True)
