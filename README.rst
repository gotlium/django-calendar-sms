SMS Notification for Free on Django
===================================

.. image:: https://api.travis-ci.org/gotlium/django-calendar-sms.png?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/gotlium/django-calendar-sms
.. image:: https://coveralls.io/repos/gotlium/django-calendar-sms/badge.png?branch=master
    :target: https://coveralls.io/r/gotlium/django-calendar-sms?branch=master
.. image:: https://pypip.in/v/django-calendar-sms/badge.png
    :alt: Current version on PyPi
    :target: https://crate.io/packages/django-calendar-sms/
.. image:: https://pypip.in/d/django-calendar-sms/badge.png
    :alt: Downloads from PyPi
    :target: https://crate.io/packages/django-calendar-sms/


What's that
-----------
This reusable Django app can help you to send sms via
Google Calendar (for free) on your Django Project.


Installation:
-------------

.. code-block:: bash

    $ pip install django-calendar-sms

2. Add the ``calendar_sms`` application to ``INSTALLED_APPS`` in your settings file (usually ``settings.py``)
3. Sync database (``./manage.py syncdb``)


Demo:
----

.. code-block:: bash

    $ sudo apt-get install virtualenvwrapper
    $ mkvirtualenv django-calendar-sms
    $ git clone https://github.com/gotlium/django-calendar-sms.git
    $ cd django-calendar-sms
    $ python setup.py develop
    $ cd demo
    $ pip install -r requirements.txt
    $ python manage.py syncdb
    $ python manage.py migrate
    $ python manage.py shell


Usage:
------
1. Setup Google Account data for current website on admin panel
2. Try to send sms from shell (``./manage.py shell``):

.. code-block:: python

    >>> from calendar_sms.sms import sendSMS
    >>> print sendSMS('Hello, World!')


Send SMS in background:
-----------------------
1. Install ``django-celery``:

.. code-block:: bash

    $  pip install django-celery

2. Add the ``djcelery`` application to ``INSTALLED_APPS`` in settings.py
3. Add django-calendar-sms configuration into project settings:

.. code-block:: python

    CELERY_IMPORTS = ('calendar_sms',)

4. Sync database (``./manage.py syncdb``)
5. Run Rabbit-MQ:

.. code-block:: bash

    $  sudo rabbitmq-server -detached

6. Run celery daemon in project directory:

.. code-block:: bash

    $  nohup python manage.py celery worker >& /dev/null &

7. Try to send sms:

.. code-block:: python

    >>> from calendar_sms.tasks import SMSSend
    >>> SMSSend.delay('Hello, World (background task)!')


| **You can use multi accounts on one or several sites**


Compatibility:
-------------
* Python: 2.6, 2.7
* Django: 1.3.x, 1.4.x, 1.5.x, 1.6


.. image:: https://d2weczhvl823v0.cloudfront.net/gotlium/django-calendar-sms/trend.png
    :alt: Bitdeli badge
    :target: https://bitdeli.com/free
