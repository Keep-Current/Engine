# Keep-Current

<!-- Badges section here. -->

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/48afb8557d8047c5900a04dff5cbdaaa)](https://app.codacy.com/app/Keep-Current/Engine?utm_source=github.com&utm_medium=referral&utm_content=Keep-Current/Engine&utm_campaign=badger)
[![BCH compliance](https://bettercodehub.com/edge/badge/Keep-Current/Engine?branch=master)](https://bettercodehub.com/)
[![Build Status](https://travis-ci.org/Keep-Current/Engine.svg?branch=master)](https://travis-ci.org/Keep-Current/Engine)

## Recommendation Engine

This repository is the documents personalized recommendation engine of the [Keep-Current project](#keep-current-project).

### Potential tools to implement

We lean heavily on existing tools as well as developing new methods. We are colaborating through Google Colab notebooks.

- [TextBlob](http://textblob.readthedocs.io/en/dev/)
- [spaCy](https://spacy.io/)
- [NLTK](https://www.nltk.org/)
- [Vowpal Wabbit](https://github.com/JohnLangford/vowpal_wabbit/wiki)

### Getting started

for running this project locally, you need first to install the dependency packages.
To install them, you can use

- [pipenv](https://docs.pipenv.org/)
- [anaconda](https://anaconda.org/)
- [virtualenv](https://virtualenv.pypa.io/en/stable/)

#### Installation using pipenv (which combines virtualenv with pip)

Install pipenv

```bash
# if you haven't installed pip
sudo easy_install pip
# install pipenv
pip install pipenv

# with homebrew (on macOS)
brew install pipenv
```

Install the packages and run the server

```bash
# install all packages
pipenv install
# run the server
pipenv run python manage.py server
```

#### Installing using Anaconda

If you have anaconda installed, it's recommended to create an environment for the project, and install the dependencies in it.

```bash
# create the environment
conda create -q -n web-miner python=3.6

# activate the environment
source activate web-miner

# install the packages
pip install -r requirements.txt
```

and test your installation by running the web server:

```bash
# start server
flask run python manage.py server
```

### Architecture

### Project Architecture

We follow the [clean architecture style](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html) and structure the codebase accordingly.

![cleanArchitecture image](https://cdn-images-1.medium.com/max/1600/1*B7LkQDyDqLN3rRSrNYkETA.jpeg)

_Image credit to [Uncle Bob](https://8thlight.com/blog/uncle-bob/)_

Most important rule:

> Source code dependencies can only point inwards. Nothing in an inner circle can know anything at all about something in an outer circle. In particular, the name of something declared in an outer circle must not be mentioned by the code in the an inner circle. That includes, functions, classes. variables, or any other named software entity.

## Who are we?

This project intends to be a shared work of meetup members, with the purpose, beside the obvious result, to also be used as a learning platform, while advancing the Natural Language Processing / Machine Learning field by exploring, comparing and hacking different models.

Please visit

- the project board on [Github](https://github.com/orgs/Keep-Current/projects)
- the repository board on [Github](https://github.com/Keep-Current/Engine/projects)
- our chat room on [Slack](https://keep-current.slack.com). If you're new, you can join using [this link](https://join.slack.com/t/keep-current/shared_invite/enQtMzY3Mzk1NjE2MzIzLWZlZWFjMDM1YWYxYmI5ZWE4YmZjNWYzMmNjMzlhMDYzOTIxZDViODhmNTMzZDI0NThmZWVlOTRjNjczZGJiOWE)
- our [facebook group](https://www.facebook.com/groups/308893846340861/) where we discuss and share current topics also outside of the project

for more.

## How to Contribute

You can find our Project board here on [GitHub](https://github.com/Keep-Current/Engine/projects) and we use [Slack](https://keep-current.slack.com) as our communication channel. If you're new, you can join using [this link](https://join.slack.com/t/keep-current/shared_invite/enQtMzY4MTA0OTQ0NTAzLTcxY2U5NmIwNmM0NmU2MmMyMWQ0YTIyMTg4MWRjMWUyYmVlNWQxMzU3ZWJlNjM4NzVmNTFhM2FjYjkzZDU3YWM)

We welcome anyone who would like to join and contribute.

Please see our [contribute guide](CONTRIBUTING.md).

We meet regularly every month in Vienna through

- the [Data Science Cafe meetup of the VDSG](https://www.meetup.com/Vienna-Data-Science-Group-Meetup/) or
- the [WeAreDevelopers :: Keep-Current meetup](https://www.meetup.com/WeAreDevelopers/)

to show our progress and discuss the next steps.

## Keep-Current Project

After studying a topic, keeping current with the news, published papers, advanced technologies and such proved to be a hard work.
One must attend conventions, subscribe to different websites and newsletters, go over different emails, alerts and such while filtering the relevant data out of these sources.

In this project, we aspire to create a platform for students, researchers, professionals and enthusiasts to discover news on relevant topics. The users are encouraged to constantly give a feedback on the suggestions, in order to adapt and personalize future results.

The goal is to create an automated system that scans the web, through a list of trusted sources, classify and categorize the documents it finds, and match them to the different users, according to their interest. It then presents it as a timely summarized digest to the user, whether by email or within a site.

If you wish to assist in different aspects (Data Engineering / Web development / DevOps), we have divided the project to several additional repositories focusing on these topics:

- The mining of data is done in the [Web-Miner repository](https://github.com/Keep-Current/web-miner)
- Web Development & UI/UX experiments can be found in our [App repository](https://github.com/Keep-Current/WebApp)
- Data Engineering tasks are more than welcomed in our [Data Engineering repository](https://github.com/Keep-Current/Data-Engineering)
- Devops tasks are all across the project. This project is developed mostly in a serverless architecture. Using Docker and Kubernetes enables freedom in deploying it on different hosting providers and plans.

_Feel free to join the discussion and provide your input!_

## About Machine Learning

### Machine Learning & Natural Language Processing

If you're new to Machine Learning, we suggest reading the following sources:

- [Machine learning collection](https://github.com/collections/machine-learning)
- [Natural Language Processing in Python Book](http://nltk.org/book/)
- [Keon's awesome-nlp!](https://github.com/keon/awesome-nlp)

[travis-badge-url]: https://travis-ci.org/liadmagen/Keep-Current.svg?branch=master
