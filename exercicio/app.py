from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

dados = {
    'titulos':[],
    'artistas':[],
    'generos':[],
    'duracoes':[]
}
@app.route("/formulario", methods= ['GET','POST'])
def formulario():


    if request.method == "POST":
        titulo = request.form['Titulo']
        dados['titulos'].append(titulo)
        artista = request.form['Artista']
        dados['artistas'].append(artista)
        genero = request.form['Genero']
        dados['generos'].append(genero)
        duracao = request.form['Duracao']
        dados['duracoes'].append(duracao)
        return render_template('formulario.html')
    else:
        return render_template('formulario.html')

@app.route("/tabela")
def tabela():
    return render_template('tabela.html', dados=dados, qtdreps = len(dados['titulos']))


if __name__ == '__main__':
    app.run(debug=True)

