#!/bin/sh
# wait_for_mysql.sh

set -e

HOST="$MYSQL_HOST"
PORT=3306

echo "Waiting for MySQL at $HOST:$PORT..."

until nc -z "$HOST" "$PORT"; do
  echo "MySQL is unavailable - sleeping"
  sleep 2
done

echo "MySQL is up - executing command"
exec "$@"
