from DAOLayer.DataAcessObject import db


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _amount = db.Column(db.Float, nullable=False)
    _type = db.Column(db.String(200), nullable=False)
    parent_id = db.Column(db.Integer)

    def __init__(self, id, amount, type, parent_id=None):
        self.id = id
        self.amount = amount
        self.type = type
        self.parent_id = parent_id

    def __repr__(self) -> str:
        return f'Transaction id - {self.id} with amount - {self._amount}'
    

db.create_all() 