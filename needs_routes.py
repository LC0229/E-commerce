from flask import request, render_template, redirect, url_for, Blueprint
from models import Need
from app import db

needs_routes = Blueprint("needs", __name__, template_folder="templates")


@needs_routes.route('/', methods=['GET','POST'])
def index():
    if request.method == "GET":
        needs = Need.query.all()
        return render_template('needs.html', needs=needs)
    elif request.method == "POST":
        id = request.form.get('id')
        title = request.form.get('title')
        description = request.form.get('description')

        need = Need(id=id, title=title, description=description)

        db.session.add(need)
        db.session.commit()

        needs = Need.query.all()
        return render_template('needs.html', needs=needs)
    

@needs_routes.route('/details/<id>', methods = ['GET'])
def details(id):
    product = Need.query.filter(Need.id == id).first()
    return render_template('details.html', product = product)