import os
from setuptools import setup
from calendarsms import VERSION

f = open(os.path.join(os.path.dirname(__file__), 'README'))
readme = f.read()
f.close()

setup(
	name='django-calendar-sms',
	version=".".join(map(str, VERSION)),
	description='This reusable Django app can help you to send sms via Google Calendar.',
	keywords = "django sms",
	long_description=readme,
	author="GoTLiuM InSPiRiT",
	author_email='gotlium@gmail.com',
	url='http://github.com/gotlium/django-calendar-sms',
	packages=['calendarsms'],
	include_package_data=True,
	install_requires=['setuptools', 'gdata', 'django'],
	zip_safe=False,
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Web Environment',
		'Framework :: Django',
		'Intended Audience :: Developers',
		'License :: GPL',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		],
)
