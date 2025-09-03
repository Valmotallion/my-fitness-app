# ACEestFitness and Gym Application  🏋️ My Fitness App

A fitness tracking web application built with   Flask  , containerized using   Docker  , and tested with   pytest  .  
It provides a simple foundation to log workouts, view progress, and can be extended into a full-fledged fitness tracker.
This is a Flask web application developed as part of a DevOps assignment to demonstrate proficiency in version control, containerization, and CI/CD pipelines.

## Project Overview
The application provides basic fitness tracking functionalities, allowing users to add workouts and their durations and view a list of all logged workouts.

## ✨ Features

- 🖥️   Flask Web App   with Jinja2 templates  
- 📂 Modular project structure (`myapp/` for source, `tests/` for test suite)  
- 🐳   Dockerized   for reproducible builds and deployment  
- ⚡ Runs with   Gunicorn   in production-ready mode  
- ✅ Integrated   pytest   tests  
- 📦 Ready for   CI/CD   using GitHub Actions  

 
## 📂 Project Structure

my-fitness-app/
├── myapp/                 # Main application package
│   ├──   init  .py
│   ├── app.py             # Flask entry point
│   └── templates/         # HTML templates
│       └── index.html
├── tests/                 # Unit tests
│   └── test\_app.py
├── venv/                  # Local virtual environment (ignored in Docker)
├── requirements.txt       # Python dependencies
├── Dockerfile             # Container definition
├── .dockerignore          # Exclude files from Docker build context
├── .gitignore             # Ignore venv, pycache, etc.
├── README.md              # Project documentation



## ⚙️ Requirements

- [Python 3.12+](https://www.python.org/)  
- [Docker](https://www.docker.com/)  
- (Optional) [pipenv / venv](https://docs.python.org/3/library/venv.html) for local development  

  

## 🚀 Getting Started (Local Development)

1. Clone the repo:

   bash
   git clone https://github.com/your-username/my-fitness-app.git
   cd my-fitness-app

2. Create and activate virtual environment:

   bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   
   
3. Install dependencies:

   bash
   pip install -r requirements.txt
   

4. Run the app:

   bash
   flask --app myapp run
   

   App will be available at:
   👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

  

## 🐳 Running with Docker

1. Build the image:

   bash
   sudo docker build -t my-fitness-app:local .
   

2. Run the container:

   bash
   sudo docker run --rm -p 5050:5000 my-fitness-app:local
   

3. Open in browser:

   👉 [http://localhost:5050](http://localhost:5050)

  

## 🧪 Running Tests

### Locally:

bash:
pytest -q


### Inside Docker:

bash
sudo docker run --rm my-fitness-app:local pytest -q
  

## ⚡ Deployment

This app runs with   Gunicorn   inside Docker, making it production-ready out of the box.
You can deploy it on any container platform:

 Heroku (via Docker)  
 AWS ECS / Fargate  
 Google Cloud Run  
 Azure App Service  
  Or a VPS with Docker installed

  

## 🛠️ GitHub Actions (CI/CD)

A sample GitHub Actions workflow (`.github/workflows/ci.yml`) can be used to:

* Run tests on every push
* Build Docker image
* Optionally push image to Docker Hub or GitHub Container Registry

Example workflow:

yaml
name: CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build-test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.12"

    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Run tests
      run: pytest -q

  docker-build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Build Docker image
      run: docker build -t my-fitness-app:ci .


👨‍💻 Author

Developed by Aniruddha Mitra for SEZG514 Devops assignment
