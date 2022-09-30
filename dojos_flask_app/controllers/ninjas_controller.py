from crypt import methods
from dojos_flask_app.models.ninja_model import Ninja
from dojos_flask_app.models.dojo_model import Dojo
from dojos_flask_app import app
from flask import render_template, redirect, request 

@app.route('/ninjas')
def form_ninja():
    all_dojos = Dojo.all_dojos()
    return render_template('ninjas.html', all_dojos=all_dojos)


@app.route("/created_ninja", methods=['POST'])
def created_ninja():
    print(request.form, "CONTIENE")
    id_ninja = Ninja.created_ninja(request.form)
    data = {
        "id": id_ninja
    }
    ninja = Ninja.get_ninja(data)
    print(ninja, "CONTIENE")
    return redirect(f'/dojos/{ninja.dojo_id}')
