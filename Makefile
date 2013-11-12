test:
	django-admin.py test --settings=calendar_sms.test_settings calendar_sms
coverage:
	export DJANGO_SETTINGS_MODULE=calendar_sms.test_settings && \
	coverage run --branch --source=calendar_sms `which django-admin.py` test calendar_sms && \
	coverage report --omit="calendar_sms/test*,calendar_sms/migrations/*,calendar_sms/management/*"
pep8:
	flake8 --exclude=migrations calendar_sms
sphinx:
	cd docs && sphinx-build -b html -d .build/doctrees . .build/html
