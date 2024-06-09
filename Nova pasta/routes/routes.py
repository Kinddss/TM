from flask import Blueprint, render_template, url_for, session, request, redirect
from app.models import Player
from data.data import fake_list
import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'usuarios_cadastrados'

)

home_route = Blueprint('home', __name__)

@home_route.route('/')
def index():

    summoner_names = fake_list()

    return render_template('index.html', summoner_names=summoner_names)
#-------------------------------------------
@home_route.route('/player/<summoner_name>')
def player_info(summoner_name):
    
    for player_info in fake_list():
        if player_info['summoner_name'] == summoner_name:
            return render_template ('player.html', player_info=player_info)
    
    return render_template('player.html', player_info={'summoner_name': summoner_name, 'level': 'N/A', 'rank': 'N/A'})

@home_route.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['password']

        if email == 'teste@teste.com' and senha == "1234":
            session['email'] = email
            return redirect(url_for('home.index'))
        else:
            error_message = "credenciais invalidas"
            return render_template('login.html', error_message=None)
    
    return render_template('login.html', error_message=None)

@home_route.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@home_route.route('/cadastro', methods=['POST'])
def submit():
    
    cursor = conexao.cursor()

    cad_nome_usuario = request.form['nome_user']
    cad_invoc = request.form['nome_inv']
    elo = request.form['elo']
    senha = request.form['password']

    commmand = f'INSERT INTO usuarios (nome_de_usuario, nome_de_invocador, rank, senha) VALUES("{cad_nome_usuario}", "{cad_invoc}", "{elo}", "{senha}")'

    cursor.execute(commmand)

    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect('/login.html')

