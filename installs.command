#!/bin/bash
cd "$(dirname "$0")"

pip3 install pycountry

pip3 uninstall googletrans
pip3 install googletrans==4.0.0rc1
