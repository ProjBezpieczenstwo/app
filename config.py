class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin@postgresDB:5432/ariusDB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '6e48ff4302924803ba0df47c2e307c78'
    EMAIL_SERVICE_URL = "http://email_service:5001"
    # JWT_SECRET_KEY = 'your-jwt-secret-key'
