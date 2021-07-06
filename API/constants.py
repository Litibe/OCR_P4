import os
import pytz

CURRENT_DIR = os.path.dirname(os.path.dirname(__file__))
EXPORT_DIR = os.path.join(CURRENT_DIR, "EXPORT_PDF")
if not os.path.exists(EXPORT_DIR):
    os.makedirs(EXPORT_DIR)

NUMBER_OF_ROUNDS = 4
TIME_ZONE = pytz.timezone('Europe/Paris')