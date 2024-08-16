from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Initialize the Flask application
app = Flask(__name__)

# Load configurations from config.py
app.config.from_object(Config)

# Initialize the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import and register blueprints from the controllers
from controllers.absensi_controller import absensi_bp
from controllers.karyawan_controller import karyawan_bp
from controllers.lokasi_controller import lokasi_bp
from controllers.muka_karyawan_controller import muka_karyawan_bp

app.register_blueprint(absensi_bp, url_prefix='/api/absensi')
app.register_blueprint(karyawan_bp, url_prefix='/api/karyawan')
app.register_blueprint(lokasi_bp, url_prefix='/api/lokasi')
app.register_blueprint(muka_karyawan_bp, url_prefix='/api/muka_karyawan')

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
