def analyze_file(file_path):
    # Contoh analisis sederhana
    with open(file_path, 'rb') as file:
        content = file.read()
        if b'backdoor' in content:
            return 'Malware Detected'
        return 'File is Safe'
