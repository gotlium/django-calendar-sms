from setuptools import setup
from calendar_sms import VERSION


setup(
    name='django-calendar-sms',
    version=".".join(map(str, VERSION)),
    description='This reusable Django app can help you to send sms via '
                'Google Calendar.',
    keywords="django sms",
    long_description=open('README').read(),
    author="GoTLiuM InSPiRiT",
    author_email='gotlium@gmail.com',
    url='http://github.com/gotlium/django-calendar-sms',
    packages=['calendar_sms'],
    package_data={'calendar_sms': [
        'locale/ru/LC_MESSAGES/django.*',
    ]},
    include_package_data=True,
    install_requires=['setuptools', 'gdata', 'django'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
