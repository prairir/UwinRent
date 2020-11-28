#!/bin/bash

wget https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux64.tar.gz

tar -xvzf geckodriver-v0.28.0-linux64.tar.gz 

chmod +x geckodriver

sudo mv geckodriver /usr/local/bin/geckodriver

rm geckodriver-v0.28.0-linux64.tar.gz
