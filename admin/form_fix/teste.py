"""

from main import app, database
from models import Usuario

# with app.app_context():
#     database.create_all()

# with app.app_context():
#     usuario= Usuario(username= "Vitor", email="vitor@hotmail.com", telefone="32999477844")
#     database.session.add(usuario)
#     database.session.commit()

# with app.app_context():
#     usuario2= Usuario(username="Teste", email="teste@teste.com", telefone="32999008533")
#     database.session.add(usuario2)
#     database.session.commit()


with app.app_context():
    meus_usuarios= Usuario.query.all()
    print(meus_usuarios)

    #pegando os dados do primeiro usuário.
    primeiro_usuario= meus_usuarios[0] #ou Usuario.query.first
    print(primeiro_usuario.username)

with app.app_context():
    # como o banco retorna uma lista, é obrigatório colocar esse ".first()" no fim, ou então coloca ".all"
    filtrando_itens= Usuario.query.filter_by(email= "vitor@hotmail.com").first()
    print(filtrando_itens.id)
    
"""