import os
import time

def delete_old_logs(log_path, age_limit=7200):  # 7200 sekund to 2 godziny
    # Sprawdzanie czasu ostatniej modyfikacji pliku
    if os.path.exists(log_path):
        file_age = time.time() - os.path.getmtime(log_path)
        if file_age > age_limit:
            os.remove(log_path)
