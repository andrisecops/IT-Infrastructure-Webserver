import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'kunci_rahasia'
    DEBUG = True
    LOG_PATH = os.path.join(os.getcwd(), 'logs')
    ALERT_EMAIL = 'admin@example.com'
    REPORT_INTERVAL = 7  # days

# Tambahkan konfigurasi lainnya yang diperlukan
