#!/bin/sh

python -m pytest --capture=no --verbose --cvo . --cov-report=html
