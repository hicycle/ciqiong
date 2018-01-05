#!/bin/bash

touch config.py manage.py
mkdir -p app/templates app/static app/main migrations tests
touch app/main/__init__.py app/main/errors.py app/main/forms.py app/main/views.py
touch app/__init__.py app/email.py app/models.py
touch tests/__init__.py tests/test.py
