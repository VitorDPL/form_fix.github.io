from form_fix import app, database
from form_fix.models import Usuario

with app.app_context():
    database.create_all()

with app.app_context():
    usuario1= Usuario(username="Vitor", email="vitor@teste.com", telefone="000")
    database.session.add(usuario1)
    database.session.commit()

#qualquer problema, é só apagar a pasta que fica o banco de dados e rodar esse arquivo aqui de novo.