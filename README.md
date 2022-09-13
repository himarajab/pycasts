## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/himarajab/pycasts.git
$ cd pycasts
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ pipenv shell
```

Then install the dependencies:

```sh
we need to have redis installed on our machine
(pycasts)$ pip install -r requirements.txt
```
Note the `(pycasts)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `pipenv`.

Once `pip` has finished downloading the dependencies:
```sh
(pycasts)$ python manage.py runserver
(pycasts)$ celery -A content_aggregator worker -l info
(pycasts)$ celery -A content_aggregator beat
```
And navigate to `http://127.0.0.1:8000/`.


## Walkthrough

APIS to aggregate data from different sources and display to users content from feed they are interested with ,also I will apply here all  technolgies I learn 