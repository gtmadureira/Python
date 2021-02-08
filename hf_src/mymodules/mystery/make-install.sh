#!/bin/bash
python setup.py sdist
pip3 install ./dist/mystery-1.0.tar.gz
pip3 install ./dist/mystery-1.0.tar.gz --upgrade