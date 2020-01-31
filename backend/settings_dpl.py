from .settings import *
import os

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
ALLOWED_HOSTS.append("40.76.72.252") #CHANGE to maching ip or domain
DEBUG = False