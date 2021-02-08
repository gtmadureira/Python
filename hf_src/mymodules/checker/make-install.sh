#!/bin/bash
python setup.py sdist
pip3 install ./dist/checker-1.0.tar.gz
pip3 install ./dist/checker-1.0.tar.gz --upgrade