from flask import jsonify, request
from Controller.Transactions import app
from Model.Transactions import Transaction, db
from sqlalchemy import text


def create_transaction(transaction_id):
    """
    Service to create a transaction
    entity in the MySQL Database
    """

    data = request.json
    amount = data.get('amount')
    type = data.get('type')
    parent_id = data.get('parent_id')

    if amount is None or type is None:
        return jsonify({"error": "Amount and type are required"}, 400)

    # Check if the transaction ID already exists
    existing_transaction = Transaction.query.get(transaction_id)
    if existing_transaction:
        return jsonify({"error": "Transaction ID already exists"}, 400)

    # Create and insert the transaction into the database
    new_transaction = Transaction(id=transaction_id, amount=amount, type=type, parent_id=parent_id)
    db.session.add(new_transaction)
    db.session.commit()

    return jsonify({"status": "ok"}, 200)



def get_transaction(transaction_id):
    """
    Service to get a transaction
    entity by it's id from database
    """
    query = text("SELECT amount, type, parent_id FROM transaction WHERE id = :transaction_id")
    transaction = db.engine.execute(query, transaction_id=transaction_id)

    if transaction:
        response_data = {
            "amount": transaction.amount,
            "type": transaction.type,
            "parent_id": transaction.parent_id
        }
        return jsonify(response_data)
    
    return jsonify({"error": "Transaction not found"}, 404)


def get_transaction_ids_by_type(type):
    """
    Service to get all transaction ids
    with same transaction type from our
    database.
    """
    query = text("SELECT id FROM transaction WHERE type = :type")
    result = db.engine.execute(query, type=type)

    ids = [row.id for row in result]
    return jsonify(ids, 200)


def calculate_transaction_sum(transaction_id):

    """
    Service to calculate the sum of
    amount of transaction by id and 
    all it's descendant
    """

    # Using a recursive Common Table Expression (CTE) to calculate the sum of linked transactions
    query = text(
        '''
        WITH RECURSIVE transaction_cte AS (
            SELECT id, amount FROM transaction WHERE id = :transaction_id
            UNION ALL
            SELECT t.id, t.amount
            FROM transaction_cte c
            JOIN transaction t ON c.id = t.parent_id
        )
        SELECT SUM(amount) AS total FROM transaction_cte
        '''
    )
    result = db.engine.execute(query, transaction_id=transaction_id)

    # Fetch the sum
    row = result.fetchone()

    if row:
        response_data = {"sum": row.total}
        return jsonify(response_data, 200)
    
    return jsonify({"error": "Transaction not found"}, 404)