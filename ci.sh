#!/bin/sh

python -m pytest --capture=no --verbose --cov . --cov-report=html
