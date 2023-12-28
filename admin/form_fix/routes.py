from flask import render_template, flash, redirect, url_for, request
from form_fix import app, database
from form_fix.forms import FormLogin
from form_fix.models import Usuario

@app.route("/", methods=['GET', 'POST'])
def login():
    form_login= FormLogin()

    if form_login.validate_on_submit() and 'botao_submit' in request.form: #Essa linha após o and ''Pergunta'' se o botao_submit está dentro do formulário.

        # pegando as informações para o bd
        # obs: para pegar as informações da classe form_login (LEMBRANDO QUE FORM_LOGIN É O FORMULÁRIO, NAO O BANCO.), é necessário colocar o .data no final.
        usuario= Usuario(username= form_login.username.data, email= form_login.email.data, telefone= form_login.telefone.data, peca_42= form_login.peca_42.data, peca_44= form_login.peca_44.data, peca_46= form_login.peca_46.data, peca_48= form_login.peca_48.data, peca_50= form_login.peca_50.data, peca_52= form_login.peca_52.data, peca_54= form_login.peca_54.data, peca_56= form_login.peca_56.data, peca_58= form_login.peca_58.data, peca_60= form_login.peca_60.data, peca_62= form_login.peca_62.data, peca_64= form_login.peca_64.data)

        #adicionando o usuario
        database.session.add(usuario)

        #comitando inormações
        database.session.commit()

        flash(f'Obrigado pela preferência, {form_login.username.data} ! Em breve você receberá mensagens contendo as promoções da loja !', 'alert-success')
        return redirect(url_for('agradecimento'))
    return render_template('login.html', form_login = form_login)

@app.route("/fim")
def agradecimento():
    return render_template("obrigado.html")
