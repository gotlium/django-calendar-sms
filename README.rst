SMS Notification for Free on Django
===================================

.. image:: https://api.travis-ci.org/gotlium/django-calendar-sms.png?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/gotlium/django-calendar-sms

What's that
-----------
This reusable Django app can help you to send sms via
Google Calendar (for free) on your Django Project.


Installation:
-------------
1. Package:

.. code-block:: bash

    $ git clone https://github.com/gotlium/django-calendar-sms.git

    $ cd django-calendar-sms && sudo python setup.py install

**OR**

.. code-block:: bash

    $  sudo pip install django-calendar-sms

2. Add the ``calendar_sms`` application to ``INSTALLED_APPS`` in your settings file (usually ``settings.py``)
3. Sync database (``./manage.py syncdb``)


Usage:
------
1. Setup Google Account data for current website on admin panel
2. Try to send sms from shell (``./manage.py shell``):

    >>> from calendar_sms.calendar_sms import sendSMS
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

    >>> from calendar_sms.tasks import SMSSend
    >>> SMSSend.delay('Hello, World (background task)!')


**You can use multi accounts on one or several sites**



.. image:: https://d2weczhvl823v0.cloudfront.net/gotlium/django-calendar-sms/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

