import os

os.system("python manage.py makemigrations --noinput")
os.system("python manage.py migrate --noinput")
