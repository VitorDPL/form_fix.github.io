# o __init__.py será executado automaticamente sempre que a pasta form_fix for chamada.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '3844731c0519f3c487f01a30c5379bb660c6607d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fix.db'

database= SQLAlchemy(app)

# percebe-se que o único programa a rodar automaticamente é o __init__.py, logo, os outros arquivos (forms, models, routes), não executarão, ou seja, seriam inexistentes na aplicação.
# ele rodaria o app, criaria tudo, mas não executaria as rotas, por exemplo.
# para resolver isso, basta:


from form_fix import routes

# OBS: precisa ser importado EMBAIXO mesmo, visto que para as rotas funcionarem, o app já deve estar criado.