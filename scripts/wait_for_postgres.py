import os
import logging
from time import time, sleep
import psycopg2
check_timeout = os.getenv("POSTGRES_CHECK_TIMEOUT", 30)
check_interval = os.getenv("POSTGRES_CHECK_INTERVAL", 1)
interval_unit = "second" if check_interval == 1 else "seconds"

start_time = time()
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

try:
  config = {
      "dbname": os.getenv("DJANGO_DB", "postgres"),
      "user": os.getenv("DJANGO_DB_USER", "postgres"),
      "password": os.getenv("DJANGO_DB_PASSWORD", ""),
      "host": os.getenv("DJANGO_DB_HOST", "db")
  }
except:
  logger.info("DB environments variables required")

def pg_isready(host, user, password, dbname):
    while time() - start_time < check_timeout:
        try:
            conn = psycopg2.connect(**vars())
            logger.info("Postgres is ready! ✨ 💅")
            conn.close()
            return True
        except psycopg2.OperationalError:
            logger.info(f"Postgres isn't ready. Waiting for {check_interval} {interval_unit}...")
            logger.info(f"Arguments {host}, {user}, {password}, {dbname}")
            sleep(check_interval)

    logger.error(f"We could not connect to Postgres within {check_timeout} seconds.")
    return False


pg_isready(**config)
