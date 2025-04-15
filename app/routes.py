from flask import jsonify, Blueprint
import pandas as pd
from app.models import SalesModel, db


# Blueprint Creation
sales_bp = Blueprint('sales_bp', __name__)


# Summary Route
@sales_bp.route('/summary', methods = ['GET'])
def sales_data_summary():
    sales_data = pd.read_sql(SalesModel.query.statement, db.engine)
    summary_data = sales_data.groupby('product_name').agg(
        total_quantity = ('quantity', 'sum'),
        average_price = ('price', 'mean')
    ).reset_index()
    return jsonify(summary_data.to_dict(orient='records'))

# Filter by product Route
@sales_bp.route('/by-product/<product_name>', methods = ['GET'])
def filter_by_product(product_name):
    filter_data = pd.read_sql(SalesModel.query.filter_by(product_name=product_name).statement, db.engine)
    return jsonify(filter_data.to_dict(orient='records'))

