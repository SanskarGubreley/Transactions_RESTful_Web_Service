from Controller.Transactions import app
from flask_sqlalchemy import SQLAlchemy

# Configure the MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Admin@123@localhost:3306/yourdatabase'
db = SQLAlchemy(app)