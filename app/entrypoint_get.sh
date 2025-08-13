#!/usr/bin/env bash
set -e

until pg_isready -h db -p 5432; do
  echo "Waiting for database..."
  sleep 2
done

python - << 'EOF'
from EarthPopulation.db import Base, engine
Base.metadata.create_all(engine)
EOF

python -m EarthPopulation.loader