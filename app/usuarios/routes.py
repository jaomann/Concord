from app import db
from app.usuarios.forms import CadastroForm
from app.models import Usuario
from app.usuarios import usuario
from flask import render_template

@usuario.route("/login")
def login():
    #rota de login para ser preenchida.
    pass

@usuario.route("/cadastro", methods=["GET", "POST"])
def novo():
    form = CadastroForm()
    if form.validate_on_submit():
        m = Usuario()
        m.nome = form.nome.data
        m.email = form.email.data

        db.session.add(m)
        db.session.commit()
        return "Usuario cadastrado"
    return render_template("cadastro.html", form=form)
