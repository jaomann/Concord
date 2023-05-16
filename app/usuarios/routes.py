from app import db
from app.main import main
from app.usuarios import usuario
from app.usuarios.forms import LoginForm, CadastroForm, InicioForm
from app.models import Usuario
from flask_login import login_user, logout_user
from flask import session,render_template, redirect, url_for
from flask_socketio import join_room, leave_room, send, emit
from manage import socketio

@usuario.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        senha = form.senha.data

        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and usuario.verifica_senha(senha):
            login_user(usuario)
            return redirect(url_for('usuario.inicio'))
        return 'Usuário ou senha inválidos'
    return render_template("login.html", form=form)


@usuario.route('/registro', methods=['GET','POST'])
def registro():
    form = CadastroForm()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        nascimento = form.nascimento.data
        estado = form.uf.data
        pais = form.origem.data
        senha = form.senha.data
        usuario = Usuario(nome=nome, nascimento=nascimento, estado=estado, pais=pais, email=email, senha=senha)
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('usuario.login'))
    return render_template('cadastro.html', form=form)

@usuario.route('/inicio', methods=['GET','POST'])
def inicio():
    form = InicioForm()
    if form.validate_on_submit():
        session['sala'] = form.sala.data
        return redirect(url_for('usuario.chat'))
    return render_template('inicio.html', form=form)
@usuario.route('/chat')
def chat():
    nome = session.get("sala")
    return render_template('rooms.html', sala=nome)

@socketio.on("entrada", namespace="/chat")
def entrada():
    nome = session.get('nome')
    sala = session.get('sala')
    join_room(sala)
    emit("status", {"msg": f"[STATUS] {nome} entrou na sala."}, room=sala)

@socketio.on("saida", namespace="/chat")
def saida(etc):
    nome = session.get('nome')
    sala = session.get('sala')
    leave_room(sala)
    emit("status", {"msg": f"[STATUS] {nome} saiu da sala."}, room=sala)

@socketio.on("msg", namespace="/chat")
def mensagem(dados):
    nome = session.get('nome')
    sala = session.get('sala')
    msg = dados['msg']
    emit('msg', {"msg": f"{nome}: {msg}"}, room=sala)
    
@usuario.route('/logout') 
def logout():
    logout_user()
    return redirect(url_for('usuario.login'))

        