# app.py

from app_instance import api
from routes import *

if __name__ == "__main__":
    api.run(port=8000, address="0.0.0.0")
