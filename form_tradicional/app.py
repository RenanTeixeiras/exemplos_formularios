from flask import Flask, render_template, request



app = Flask(__name__)


@app.route("/registro", methods = ['GET', 'POST'])
def registro():
    if request.method == "POST":
        nome = request.form['name']
        password = request.form['password']
        email = request.form['email']
        return render_template('usuario.html', nome = nome, email=email, senha = password)
    else:
        return render_template('registro.html')

if __name__ == "__main__":
    app.run(debug=True)