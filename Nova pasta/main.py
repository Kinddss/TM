from flask import Flask, url_for, render_template
from routes.routes import home_route

#inicializacao
app = Flask(__name__)
app.secret_key = 'senhasecreta'
app.register_blueprint(home_route)

#execucao do programa
app.run(debug=True)