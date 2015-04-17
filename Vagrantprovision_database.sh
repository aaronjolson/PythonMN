#!/bin/sh

echo "Setup a database ..."
echo "If this appears hung, then Postgres has an open connection. Shut down the Django test server."
# This is required to fix LATIN1 as the default LANG on the preceise64 box on Vagrant
pg_dropcluster --stop 9.3 main ; pg_createcluster --start --locale en_US.UTF-8 9.3 main
cat << EOF | su - postgres -c psql
-- Create the user:
CREATE USER python PASSWORD 'python' CREATEDB;

-- Create the database:
CREATE DATABASE python WITH owner = python ENCODING = 'utf-8';

-- Grant privileges to the user
GRANT ALL PRIVILEGES ON DATABASE python TO python;
EOF

cd /home/vagrant
echo "export DATABASE_URL=postgres://python:python@localhost:5432/python" >> /home/vagrant/.profile

echo "Setup Django app database (syncdb, migrate, loaddata)."
cd /vagrant
python manage.py syncdb --noinput --settings=PythonMN_Landing.settings
python manage.py migrate --settings=PythonMN_Landing.settings