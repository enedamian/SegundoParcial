from flask import Flask
from modelo.producto import inicializar_productos

from controlador.rutas_producto import productos_bp

app = Flask(__name__) #creamos una instancia de la clase Flask

inicializar_productos()

# registramos el blueprint

app.register_blueprint(productos_bp)

if __name__ == '__main__':
    app.run(debug=True) #iniciamos la aplicación