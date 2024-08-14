import random

def get_dashboard_data():
    # Contoh data, ganti dengan data yang diambil dari sistem
    data = {
        'traffic_in': random.randint(100, 1000),
        'traffic_out': random.randint(100, 1000),
        'threats_detected': random.randint(0, 5),
        'alerts': random.randint(0, 3),
    }
    return data
