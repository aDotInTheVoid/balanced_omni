from .settings import *
import os

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
ALLOWED_HOSTS.append("40.71.19.82") #CHANGE to maching ip or domain
DEBUG = False