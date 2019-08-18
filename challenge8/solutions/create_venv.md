# Prerequisites for Challenge 8
 
## Create and Activate Virtual Environment

Check current Python version:

```bash
python -V
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:
 - Activate it on Windows: ```.\.venv\Scripts\activate```
 - Activate it on Linux: ```. .venv/bin/activate```
 
Install 3rd-Party module 'requests' (required for this challenge):

```bash
python -m pip install requests
```

## Sharing your program's dependencies:

Create a requirements file:
```bash
python -m pip freeze > requirements.txt
```

The [requirements.txt](requirements.txt) file can be distributed and used to install the exact same packages at the correct version elsewhere.
 
