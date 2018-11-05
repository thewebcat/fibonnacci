#!/bin/sh
set -e

# Collect static files
if [ "x$DJANGO_MANAGE_COLLECTSTATIC" = 'xon' ]; then
    echo "Collect static files"
    python -m fibonacci collectstatic --noinput
fi

# Apply database migrations
if [ "x$DJANGO_MANAGE_MIGRATE" = 'xon' ]; then
    echo "Apply database migrations"
    python -m fibonacci migrate
fi

exec "$@"
