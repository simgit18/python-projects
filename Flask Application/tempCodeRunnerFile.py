app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:%s@localhost/height_collecter" % urlquote('Son@devi1')
db = SQLAlchemy(app)