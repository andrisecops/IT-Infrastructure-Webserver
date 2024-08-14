from flask import render_template
from app import app
from app.dashboard import get_dashboard_data

@app.route('/')
def index():
    data = get_dashboard_data()
    return render_template('dashboard.html', data=data)

# Tambahkan rute lainnya yang diperlukan
