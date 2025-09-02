# ACEestFitness and Gym Application

This is a Flask web application developed as part of a DevOps assignment to demonstrate proficiency in version control, containerization, and CI/CD pipelines.

## Project Overview

The application provides basic fitness tracking functionalities, allowing users to add workouts and their durations and view a list of all logged workouts.

## Local Setup

To run this application on your local machine, follow these steps:

1.  Clone the repository:
    ```bash
    git clone [https://github.com/](https://github.com/)<YOUR-USERNAME>/<YOUR-REPOSITORY-NAME>.git
    cd <YOUR-REPOSITORY-NAME>
    ```

2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4.  Run the Flask application:
    ```bash
    flask run
    ```
    The application will be accessible at `http://127.0.0.1:5000`.

## Local Testing

To run the unit tests locally using Pytest, ensure  all  dependencies are installed and then execute:

```bash
pytest


## Run locally
```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python app.py