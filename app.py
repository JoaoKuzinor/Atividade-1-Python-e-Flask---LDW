from flask import Flask, render_template
from controllers import routes

# Instancia do flask na variavel app
app = Flask(__name__, template_folder="views")
routes.init_app(app)

# Inicia o servidor
if __name__ == "__main__":
    app.run(host="localhost", port=4000, debug=True)
