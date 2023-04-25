from app import db
from app.usuarios import usuario
from app.usuarios.forms import LoginForm, CadastroForm
from app.models import Usuario
from flask_login import login_user
from flask_login import logout_user
from flask import render_template


@usuario.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        senha = form.senha.data

        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and usuario.verifica_senha(senha):
            login_user(usuario)
            return('Login efetuado com sucesso')
        return 'Usuário ou senha inválidos'
    return render_template("login.html", form=form)


@usuario.route('/registro', methods=['GET','POST'])
def registro():
    form = CadastroForm()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        #senha = form.senha.data
        usuario = Usuario(nome=nome, email=email)
        db.session.add(usuario)
        db.session.commit()
        return "Usuário cadastrado com sucesso!!!"
    return render_template('cadastro.html', form=form)


@usuario.route('/logout') 
def logout():
    logout_user()

        