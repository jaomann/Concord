from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')

class CadastroForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    nascimento = StringField('Data de Nascimento', validators=[DataRequired()])
    uf = StringField('Estado')
    origem = StringField('País', validators=[DataRequired()])
    submit = SubmitField('Registrar')
    
class InicioForm(FlaskForm):
    sala = StringField('Sala: ', validators=[DataRequired()])
    submit = SubmitField('Pesquisar')