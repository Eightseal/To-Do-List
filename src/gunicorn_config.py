import multiprocessing
import os

# Binding
port = int(os.environ.get("FLASK_RUN_PORT", 80))
bind = f"0.0.0.0:{port}"
print(f"Binding to {bind}")

# Worker Processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"  # 'sync', 'gevent', 'gthread', etc.

# Threads per worker
threads = 4  # 2-4 threads per worker is usually good

# Timeouts
timeout = 120  # seconds
keepalive = 5  # seconds
graceful_timeout = 120  # seconds

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Process Naming
proc_name = "we-care"

# Security
limit_request_line = 4096
limit_request_fields = 100
limit_request_field_size = 8190

# Server Mechanics
preload_app = True
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None
