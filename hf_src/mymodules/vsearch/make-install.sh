#!/bin/bash
python setup.py sdist
pip3 install ./dist/vsearch-1.0.tar.gz
pip3 install ./dist/vsearch-1.0.tar.gz --upgrade