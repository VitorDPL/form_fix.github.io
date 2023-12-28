from form_fix import database

class Usuario(database.Model):
    id= database.Column(database.Integer, primary_key= True)
    username= database.Column(database.String, nullable= False)
    email= database.Column(database.String, nullable= False, unique= True)
    telefone= database.Column(database.Integer, nullable= False, unique= True)
    peca_42= database.Column(database.Boolean, default=False)
    peca_44= database.Column(database.Boolean, default=False)
    peca_46= database.Column(database.Boolean, default=False)
    peca_48= database.Column(database.Boolean, default=False)
    peca_50= database.Column(database.Boolean, default=False)
    peca_52= database.Column(database.Boolean, default=False)
    peca_54= database.Column(database.Boolean, default=False)
    peca_56= database.Column(database.Boolean, default=False)
    peca_58= database.Column(database.Boolean, default=False)
    peca_60= database.Column(database.Boolean, default=False)
    peca_62= database.Column(database.Boolean, default=False)
    peca_64= database.Column(database.Boolean, default=False)
