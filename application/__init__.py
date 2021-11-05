from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://robertotest@test-roberto:Password5713186@test-roberto.mysql.database.azure.com:3306/tutorial"

db = SQLAlchemy(app)

from application import routes