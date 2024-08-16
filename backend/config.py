import os
import psycopg2

class Config:
    # Set secret key for session management
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret_key'

    # Database configurations
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:123@localhost:5432/attendance_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Additional configurations
    UPLOAD_FOLDER = 'uploads/'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def create_connection():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="123",  # Ganti dengan password sebenarnya
            host="localhost",
            port="5432",
            database="attendance_db"
        )
        return connection
    except Exception as error:
        print(f"Error connecting to the database: {error}")
        return None