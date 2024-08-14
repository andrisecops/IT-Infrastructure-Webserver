import os
import logging

def monitor_incoming_files(directory):
    files = os.listdir(directory)
    for file in files:
        if file.endswith(('.php', '.exe', '.js', '.bat')):
            logging.warning(f'Threat detected in file: {file}')
            alert_admin(f'Threat detected in file: {file}')

def alert_admin(message):
    # Fungsi untuk mengirim notifikasi email
    logging.info(f'Sending alert to admin: {message}')
    # Implementasi pengiriman email di sini
