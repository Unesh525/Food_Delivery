import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('postgresql://food_delivery_user:pk7MEVGqOlIL23QOONMBJyI81hWiOv4I@dpg-d21n15nfte5s73fqlbo0-a.oregon-postgres.render.com/food_delivery_db_j3ky'))
}
