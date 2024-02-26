### Hexlet tests and linter status, Maintability:
[![Actions Status](https://github.com/Abra19/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Abra19/python-project-52/actions)
[![Python CI](https://github.com/Abra19/page_analyzer/actions/workflows/python_ci.yml/badge.svg)](https://github.com/Abra19/page_analyzer/actions/workflows/python_ci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/e08d3f09e7d1220cad9b/maintainability)](https://codeclimate.com/github/Abra19/python-project-52/maintainability)


### Descriptions
This project implements an application based on the Flask framework. The app analyses the selected pages for SEO suitability

### Requirements
1. Python >=3.10
2. poetry >= 1.2.0
3. Flask >= 3.0.0
4. gunicorn >= 20.1.0


### To get started
1. Clone git repo:
  `git clone git@github.com:Abra19/page_analyzer.git`
2. Go to directory page_analyzer:
  `cd page_analyzer`
3.  Configuring `poetry` to create a virtual environment:
  `poetry config virtualenvs.in-project true`
4.  Create virtual environment and Install dependencies
  `make install`
5. Start app 
  `make start`

### [Try the application](https://page-analyzer-f6z5.onrender.com)