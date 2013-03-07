Djang Suit contribution
=======================

This repository is **for development, testing and contribution** of `Django Suit <http://djangosuit.com/>`_ project.

**Main repository is here**: https://github.com/darklow/django-suit

Read more: http://djangosuit.com/

Documentation: http://django-suit.readthedocs.org/en/latest/


How to setup contrib project
============================

How to setup contribution environment and project using `virtualenv` and `pip`

1. Requirements:

  * Django 1.4/1.5
  * Python 2.6.6 - 3.3.0
  * lessc compiler - http://lesscss.org/
  * package requirements are in ``requirements.txt``
  * pip (or if you know alternative commands you can use ``easy_install``)

2. Setup project environment::

    # Create environment/project main directory
    mkdir djangosuit-contrib
    cd djangosuit-contrib

    # Create virtualenv
    virtualenv env --no-site-packages

    # Activate virtualenv
    . env/bin/activate

    # Clone Django Suit contrib project
    git clone https://github.com/darklow/django-suit-contrib.git djangosuit
    cd djangosuit

    # Clone Django Suit examples app
    git clone https://github.com/darklow/django-suit-examples.git examples

    # Install requirements
    pip install -r requirements.txt

3. Fork django-suit repo on Github and do following::

    # Clone forked Django Suit repo
    git clone git://github.com/YOUR_NAME/django-suit.git suit

    # Install Django Suit from local fork
    pip install -e suit

    # Sync Django DB
    ./manage.py syncdb

4. Now project is ready and you can use ``manage.py`` to start server::

    ./manage.py runserver

5. Now go to ``/admin/`` and you should see login form


Structure
---------

1. ``suit/`` - whole Django Suit package
2. ``suit/suit/`` - Django Suit app
3. ``suit/docs/`` - Django Suit Sphinx documentation
4. ``suit/suit/static/suit/less`` - Less files directory (Do not change CSS files directly)
5. You can also contribute to ``examples`` app, in that case fork it first


Less/css files handling
-----------------------

Django Suit contrib package uses `django-compressor <https://github.com/jezdez/django_compressor>`_ for less compiling (actual compiling is done by ``lessc``).

Whenever you change any of ``.less`` files, ``.css`` file is recompiled to cache andcopied to ``suit/static/suit/css/suit.css`` file. When contributing you should commit both - ``.less`` and ``suit.css`` files


Notes
-----

Page load time for contrib project could be up to 500ms. Reason of this is ``.less`` files are recompiled on every request, otherwise django-compressor won't detect changes in @imported .less files, see `issue #274 <https://github.com/jezdez/django_compressor/issues/274>`_

