import multiprocessing
import os

# Reduzir número de workers para economizar memória
workers = 2

# Reduzir timeout para evitar processos longos
timeout = 29

# Configurar max requests para reciclar workers periodicamente
max_requests = 1000
max_requests_jitter = 50

# Configurações de logging
accesslog = '-'
errorlog = '-'
loglevel = 'info'

# Usar gevent para melhor performance
worker_class = 'gevent'
worker_connections = 100

# Bind to Heroku's dynamic port
port = int(os.environ.get('PORT', 5000))
bind = f'0.0.0.0:{port}'

# Raw env
raw_env = [
    f"DATABASE_URL={os.environ.get('DATABASE_URL')}",
    f"FLASK_SECRET_KEY={os.environ.get('FLASK_SECRET_KEY')}",
    f"PGDATABASE={os.environ.get('PGDATABASE')}",
    f"PGHOST={os.environ.get('PGHOST')}",
    f"PGPORT={os.environ.get('PGPORT')}",
    f"PGUSER={os.environ.get('PGUSER')}",
    f"PGPASSWORD={os.environ.get('PGPASSWORD')}",
    f"FOR4PAYMENTS_SECRET_KEY={os.environ.get('FOR4PAYMENTS_SECRET_KEY')}"
]