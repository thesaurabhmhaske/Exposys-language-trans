# Language Translator Web Application

This is a language translator web application built using Flask in Python. The application allows users to input text or upload PDF files in one language and translate it to over 130 different languages using the Google Translate API.

## Installation

To install the necessary dependencies, run the following command:

pip install -r requirements.txt



## Usage

To start the application, run the following command:

python app.py



Then, navigate to `http://localhost:5000` in your web browser to access the application.

## Features

The following features are included in this language translator web application:

- Translate text from one language to another using the Google Translate API.
- Translate PDF files from one language to another using the Google Translate API.
- A company profile slideshow on the homepage.
- Two translating tools: Text translator and PDF translator.

## Technologies Used

The following technologies were used in building this language translator web application:

- Python 3.9
- Flask Framework
- HTML
- CSS
- JavaScript
- Google Translate API
- Render.com (for deployment)

## File Structure

The following files are included in this project:

├── app.py

├── forms.py

├── templates

│ ├── base.html

│ ├── index.html

│ ├── translate.html

│ └── translate_pdf.html

├── static

│ ├── css

│ ├── js

│ └── images

├── requirements.txt

└── Procfile



- `app.py`: This file contains the main Flask application code.
- `forms.py`: This file contains the form classes used to handle user input.
- `templates/base.html`: This file contains the base HTML template used for all pages in the application.
- `templates/index.html`: This file contains the HTML template used for the homepage.
- `templates/translate.html`: This file contains the HTML template used for the text translator.
- `templates/translate_pdf.html`: This file contains the HTML template used for the PDF translator.
- `static/css`: This directory contains the CSS files used for styling the application.
- `static/js`: This directory contains the JavaScript files used for the slideshow and form validation.
- `static/images`: This directory contains the images used in the application.
- `requirements.txt`: This file contains the list of Python dependencies required to run the application.
- `Procfile`: This file is used by Heroku to run the application.

## Deployment

This application is deployed on Render at https://language-translator.onrender.com/.

## Contributing

Contributions are welcome! Please feel free to open a pull request or submit an issue if you find a bug or have a suggestion for improvement.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
