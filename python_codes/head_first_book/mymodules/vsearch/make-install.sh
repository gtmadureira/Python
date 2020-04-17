#!/bin/bash
python3.8 setup.py sdist
sudo -H python3.8 -m pip install ./dist/vsearch-1.0.tar.gz
sudo -H python3.8 -m pip install ./dist/vsearch-1.0.tar.gz --upgrade
