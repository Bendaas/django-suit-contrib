Djang Suit contrib project
==========================

This repository is **for development**, testing and contribution of `Django Suit <http://djangosuit.com/>`_ project.

Main repository is here: https://github.com/darklow/django-suit

Read more: http://djangosuit.com/

Documentation: http://django-suit.readthedocs.org/en/latest/


How to setup contrib project
============================

How to setup contribution environment and project using `virtualenv` and `pip`

1. Setup project environment:

    # Environment root
    mkdir djangosuit-contrib
    cd djangosuit-contrib

    # Create virtualenv
    virtualenv env --no-site-packages

    # Activate virtualenv
    . env/bin/activate

    # Clone Django Suit contrib project
    git clone https://bitbucket.org/darklow/django-suit-contrib.git djangosuit
    cd djangosuit

    # Install requirements
    pip install -r requirements.txt

2. Fork django-suit repo on Github and run following:

    # Clone forked Django Suit repo
    git clone git://github.com/darklow/django-suit.git suit

    # Install Django Suit from local fork
    pip install -e suit

