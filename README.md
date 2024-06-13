# Board
This repository contains a web application built using Flask, Bootstrap, and Jinja templates. The primary purpose of this project was to learn and experiment with these technologies while creating a functional and interactive website for my second project - sclask (Web Scrapper).

## Project Overview

### Features
- **User Registration and Login**: Users can create an account and log in to access the website's features.
- **Number Generation**: A new number is generated every 5 minutes.
- **Points System**: Users can input the generated number to earn points.
- **Responsive Design**: The website uses some Bootstrap for a mobile-friendly, responsive design.

### Learning Objectives
- **Flask**: Understand the basics of Flask, including routing, templates, and user authentication.
- **Bootstrap**: Learn how to create a responsive layout and use Bootstrap components.
- **Jinja**: Implement Jinja templating for dynamic content rendering.

### Usage
1. Clone the repository
```
git clone https://github.com/abraxas-dev/board.git
```
2. Navigate to the project directory
```
cd ./board
```
3. Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
4. Install the dependencies
```
pip install -r requirements.txt
```
5. Create a .env file in the project root directory with the following content:
```
FLASK_SECRET_KEY="your secret key" # Must have letters and digits !
FLASK_DATABASE=board.sqlite
```
6. Initialize a database
```
flask --app board init-db
```
7. Run the application
```
flask --app board run # Optional --port YOURPORT
```
8. Now open the website
```
http://localhost:YOURPORT/
```

### Note
- Tested on Unix Systems.
