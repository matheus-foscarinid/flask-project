from flask import Blueprint, render_template, request, redirect, url_for
from ..models import User, db

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/')
def index():
    usuarios = User.query.all()
    return render_template('index.html', usuarios=usuarios)

@hello_bp.route('/sobre')
def about():
    return "Olá, Matheus!"

@hello_bp.route('/novoUsuario', methods=['POST'])
def novo_usuario():
    nome_usuario = request.form['nome_usuario']
    if nome_usuario:
        novo_usuario = User(username=nome_usuario)
        db.session.add(novo_usuario)
        db.session.commit()
    return redirect(url_for('hello.index'))


@hello_bp.route('/removerUsuario/<int:id_usuario>', methods=['POST'])
def remover_usuario(id_usuario):
    if id_usuario:
        usuario = User.query.get(id_usuario)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
    return redirect(url_for('hello.index'))
