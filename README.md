# Flask Learning Project - Board
This repository contains a web application built using Flask, Bootstrap, and Jinja templates. The primary purpose of this project was to learn and experiment with these technologies while creating a functional and interactive website.

## Project Overview

### Features
* User Registration and Login: Users can create an account and log in to access the website's features.
* Number Generation: A new number is generated every 5 minutes.
* Points System: Users can input the generated number to earn points.
* Responsive Design: The website uses some Bootstrap for a mobile-friendly, responsive design.

### Learning Objectives
* Flask: Understand the basics of Flask, including routing, templates, and user authentication.
* Bootstrap: Learn how to create a responsive layout and use Bootstrap components.
* Jinja: Implement Jinja templating for dynamic content rendering.

### Usage
1. Clone the repository
```
git clone https://github.com/name.git
```
2. Navigate to the project directory
```
cd your-repo-name
```
3. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
4. Install the dependencies:
```
pip install -r requirements.txt
```
5. Create a .env file in the project root directory with the following content:
```
FLASK_SECRET_KEY="your secret key"
FLASK_DATABASE=board.sqlite
FLASK_APP=app.py
```
6. Run the application
```
flask -app board run (Optional : --port 8000)
```
