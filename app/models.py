from app.extension import db

class SalesModel(db.Model):
    
    # Table Name
    __tablename__ = 'sales'
    # Field Name Intialize
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date, nullable = False)
    product_name = db.Column(db.String, nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    price = db.Column(db.Numeric, nullable = False)