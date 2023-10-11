from flask import Flask
from Services.Transactions import *
app = Flask(__name__)


@app.route('/transactionservice/transaction/<int:transaction_id>', methods=['PUT'])
def create_transaction(transaction_id):
    try:
        # Call the function to create a transaction
        result = create_transaction(transaction_id)

        return result
    except Exception as e:
        return jsonify({"error": str(e)}, 500)

@app.route('/transactionservice/transaction/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    try:
        # Call the function to get a transaction
        result = get_transaction(transaction_id)

        return result
    except Exception as e:
        return jsonify({"error": str(e)}, 500)

@app.route('/transactionservice/types/<string:type>', methods=['GET'])
def get_transaction_ids_by_type(type):
    try:
        # Call the function to get transaction IDs by type
        result = get_transaction_ids_by_type(type)

        return result
    except Exception as e:
        return jsonify({"error": str(e)}, 500)

@app.route('/transactionservice/sum/<int:transaction_id>', methods=['GET'])
def calculate_transaction_sum(transaction_id):
    try:
        # Call the function to calculate transaction sum
        result = calculate_transaction_sum(transaction_id)

        return result
    except Exception as e:
        return jsonify({"error": str(e)}, 500)
