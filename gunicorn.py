import multiprocessing

command = '/home/ubuntu/ArianAlaviWebsite/env/bin/gunicorn'
pythonpath = '/home/ubuntu/ArianAlaviWebsite'
bind = '0.0.0.0:8000'
workers = (multiprocessing.cpu_count() * 2)