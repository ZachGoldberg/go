mkdir -p parts
mkdir -p build/parts

sudo apt-get install uwsgi nginx haproxy  uwsgi-plugin-python


python bootstrap.py
echo "Now configure the top of buildout.cfg then run ./run buildout, ./run syncdb and then ./run nginx, ./run haproxy and ./run wsgi"
