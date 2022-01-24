from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(40), nullable=False)
    expire_date = db.Column(db.Date)

    def __repr__(self):
        return f"Product('{self.product_name}', '{self.expire_date}')"
