Djang Suit contrib project
==========================

This repository is **for development**, testing and contribution of `Django Suit <http://djangosuit.com/>`_ project.

Main repository is here: https://github.com/darklow/django-suit

How to setup contrib project
============================

How to setup contribution package using `virtualenv` and `pip`

1. Setup project environment:

```
# Environment root
mkdir djangosuit
cd djangosuit

# create virtualenv
virtualenv env --no-site-packages

# activate virtualenv
. env/bin/activate

# Clone Django Suit contrib project
git clone https://darklow@bitbucket.org/darklow/django-suit-contrib.git contrib
cd contrib

# install requirements
pip install -r requirements.txt

git clone git://github.com/darklow/django-suit.git suit

# clone your forked github repo
git clone git://github.com/YOUR_USERNAME/django-suit.git suit
```

2. Fork django-suit repo


Django Suit
===========

Read more: http://djangosuit.com/

Documentation: http://django-suit.readthedocs.org/en/latest/
