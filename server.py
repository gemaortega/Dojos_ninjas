from dojos_flask_app import app
from dojos_flask_app.controllers import dojos_controllers, ninjas_controller
app.secret_key="secret"


if __name__=="__main__":
    app.run(debug=True)