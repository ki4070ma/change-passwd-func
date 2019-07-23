#!/bin/sh

if ! python -m isort --check-only -rc . ; then
  echo "Please run command 'python -m isort -rc .' on your local and commit the result"
  exit 1
fi

if ! python -m autopep8 -r --global-config .config-pep8 -i . ; then
  echo "Please run command 'python -m autopep8 -r --global-config .config-pep8 -i .' on your local and commit the result"
  exit 1
fi

if ! python -m mypy . ; then
  echo "Please check and fix mypy warning"
  exit 1
fi

python -m pytest --capture=no --verbose --cov . --cov-report=html
