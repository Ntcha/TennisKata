# Tennis Kata

This kata aims to demonstrate one's technical excellence when solving a given problem, in this case, a basic tennis game.
See https://gist.github.com/MatteoPierro/22e09a2b5d9e41fdd8c226d318fc0984 for full details.


## Installation & usage
Requires python >= 3.6 ( https://www.python.org/downloads/ )

For Windows :
* \# git clone git@github.com:Ntcha/TennisKata.git
* \# cd TennisKata
* \# python3 -m venv .
* \# Scripts\activate
* (TennisKata) pip install -r requirements.txt
* python -m flake8 --exclude=Include,Lib,Scripts
* python -m pytest --ignore=Include --ignore=Lib --ignore=Scripts
* python src\main.py

For Linux : 
* \# git clone git@github.com:Ntcha/TennisKata.git
* \# cd TennisKata
* \# python3 -m venv .
* \# source bin/activate
* (TennisKata) pip install -r requirements.txt
* python3 -m flake8 --exclude=Include,Lib,Scripts
* python3 -m pytest --ignore=Include --ignore=Lib --ignore=Scripts
* python3 src/main.py

I don't have a Mac, should be similar to Linux though.
