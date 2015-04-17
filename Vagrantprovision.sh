#!/bin/sh

echo "Set sensible OS env defaults ..."
locale-gen en_US.UTF-8
update-locale LANG=en_US.UTF-8

echo "Install OS dependencies ..."
apt-get update && apt-get install -y python-dev postgresql libpq-dev libjpeg8 libjpeg62-dev redis-server git python-software-properties

echo "Running apt-get update ..."
apt-get update

echo "Install PIP  ..."
# Github doesn't send a last modified header so wget cache doesn't work
if [ ! -f /var/cache/wget/get-pip.py ]; then
    wget  -N -P /var/cache/wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
fi
cp /var/cache/wget/get-pip.py /home/vagrant/get-pip.py
cd /home/vagrant
python get-pip.py

echo "Install Requirements via PIP ..."
cd /home/vagrant
pip install --download=/var/cache/pip -r /vagrant/requirements/requirements.txt
pip install --use-wheel --no-index --find-links=/var/cache/pip --exists-action=b -r /vagrant/requirements/requirements.txt

echo "Set the default settings module in the user profile ..."
cd /home/vagrant
echo "export DJANGO_SETTINGS_MODULE=PythonMN_Landing.settings" >> /home/vagrant/.profile

echo "Run database setup script ..."
cd /vagrant
sudo bash ./Vagrantprovision_database.sh

#echo "Collect static files"
#cd /vagrant
#python manage.py collectstatic --noinput --settings=PythonMN_Landing.settings

echo "SUCCESS!"