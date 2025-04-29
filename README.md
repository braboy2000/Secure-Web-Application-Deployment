Secure Web Application Deployment with Flask

Python
Flask
AWS

This project demonstrates the deployment of a basic Flask web application on an AWS EC2 instance. The application is designed to be publicly accessible and includes unit tests to ensure proper functionality.
Key Features

    Flask Web Application: A simple Flask app serving a basic homepage

    EC2 Deployment: Hosted on an AWS EC2 Ubuntu instance for public accessibility

    Unit Testing: Uses Python's unittest framework to verify application functionality

    Python 3: Developed with Python 3 using virtual environment for package management

Project Structure

project-root/
│
├── app.py                # Main Flask application file
├── tests/                 # Test directory
│   └── test_app.py        # Unit tests for the Flask app
├── requirements.txt       # Python dependencies
└── README.md              # This documentation file

Prerequisites

    AWS EC2 Instance (Ubuntu-based)

    Python 3 installed (both local machine and EC2 instance)

    GitHub repository for code storage and version control

    Basic knowledge of Flask and AWS EC2

Setup Instructions

    Clone the repository:
    bash

git clone <repository-url>
cd <project-directory>

Set up virtual environment (recommended):
bash

python3 -m venv venv
source venv/bin/activate

Install dependencies:
bash

pip install -r requirements.txt

Run the Flask application:
bash

python app.py

Run tests:
bash

    python -m unittest tests/test_app.py

Deployment on EC2

    SSH into your EC2 instance

    Clone the repository as shown above

    Install dependencies

    Run the application with:
    bash

    flask run --host=0.0.0.0 --port=5000

    Configure security groups to allow inbound traffic on port 5000

Testing

The project includes unit tests to verify:

    The homepage loads correctly

    The application returns a 200 status code for the main route

Run tests with:
bash

python -m unittest tests/test_app.py

Security Considerations

    The application is configured to run on 0.0.0.0 to make it accessible on the EC2 instance

    For production use, consider:

        Adding proper authentication

        Using HTTPS with a reverse proxy (Nginx/Apache)

        Implementing additional security headers

        Using a production WSGI server (Gunicorn, uWSGI)

License

This project is open-source and available under the MIT License.
Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
Contact

For questions or support, please open an issue in the repository.
