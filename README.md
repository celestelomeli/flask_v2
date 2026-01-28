# flask_v2

A simple Flask web application that greets users by name.

## Description

This is a basic Flask app demonstrating form handling and template rendering. Users enter their name on the home page and receive a personalized greeting.

## Project Structure

```
flask_v2/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   ├── index.html     # Home page with form
│   └── greet.html     # Greeting page
└── static/            # Static assets
    └── styles.css     # CSS styles
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/celestelomeli/flask_v2.git
cd flask_v2
```

2. (Optional but recommended) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000/`

## Usage

1. Navigate to the home page
2. Enter your name in the form
3. Click Submit to see your personalized greeting 
