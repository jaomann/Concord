from app import db
from app.usuarios.forms import CadastroForm
from app.models import Usuario
from app.usuarios import usuario
from flask import render_template

@usuario.route("/login")
def login():
    #rota de login para ser preenchida.
    pass

@Usuario.route("/cadastro")
def novo():
    form = CadastroForm()
    if form.validate_on_submit():
        m = Usuario()
        m.nome = form.nome.data
        m.email = form.email.data

        db.session.add(m)
        db.session.commit()
        return "Usuario adicionado com sucesso"
    ##return render_template("Usuario_novo.html", form=form)
    pass
