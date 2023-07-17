#!/bin/sh

pip install -r requirements.txt
pre-commit install
pre-commit install-hooks
