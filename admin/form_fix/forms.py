from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Email


class FormLogin(FlaskForm):
    username= StringField('Insira o seu nome no campo abaixo: ', validators=[DataRequired()])
    email= StringField('Insira o seu e-mail no campo abaixo: ', validators=[DataRequired(), Email()])
    telefone= IntegerField('Telefone (favor inserir o DDD)', validators=[DataRequired()])
    peca_42= BooleanField('Tamanho 42')
    peca_44= BooleanField('Tamanho 44')
    peca_46= BooleanField('Tamanho 46')
    peca_48= BooleanField('Tamanho 48')
    peca_50= BooleanField('Tamanho 50')
    peca_52= BooleanField('Tamanho 52')
    peca_54= BooleanField('Tamanho 54')
    peca_56= BooleanField('Tamanho 56')
    peca_58= BooleanField('Tamanho 58')
    peca_60= BooleanField('Tamanho 60')
    peca_62= BooleanField('Tamanho 62')
    peca_64= BooleanField('Tamanho 64')
    botao_submit= SubmitField('Resgatar a promoção')