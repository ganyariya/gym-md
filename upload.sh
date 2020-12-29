#!/usr/bin/env bash

rm -f -r gym_md.egg-info/* dist/*
python setup.py bdist_wheel
twine upload dist/*