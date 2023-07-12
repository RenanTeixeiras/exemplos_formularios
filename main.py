from flask_wtf import FlaskForm
from flask import Flask, request, render_template, url_for
from wtforms.fields import PasswordField, SubmitField, EmailField
from wtforms.validators import Length

app = Flask(__name__)
app.config['SECRET_KEY'] =  'Jesus Cristo'

class LoginForm(FlaskForm):
	email = EmailField("E-mail")
	password = PasswordField("Senha", validators=[Length(3, 6, "O campo deve conter de 3 a 6 caracteres")])
	submit = SubmitField("Logar")


@app.route("/login", methods = ['GET','POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
            email = request.form["email"]
            senha = request.form["password"]
            return render_template("usuario_logado.html", form=form,email=email)
    else:
        return render_template("login.html", form=form)


if __name__ == "__main__":
	app.run(debug=True)