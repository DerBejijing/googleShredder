#!/bin/bash
cd "$(dirname "$0")"

sudo apt-get install python3-tk

pip3 install pycountry

pip3 uninstall googletrans
pip3 install googletrans==4.0.0rc1
