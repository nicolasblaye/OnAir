from flask import Flask
from on_air.blueprints.serie_blueprint import series

app = Flask(__name__)
app.register_blueprint(series, url_prefix='/series')

