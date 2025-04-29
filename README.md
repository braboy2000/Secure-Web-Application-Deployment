# Secure Web Application Deployment with Flask

This project demonstrates the deployment of a basic Flask web application on an AWS EC2 instance. The web application is designed to be publicly accessible and includes basic testing using Python's `unittest` framework to ensure proper functionality.

## Key Features:

* **Flask Web Application:** A simple Flask app that serves a basic homepage.
* **EC2 Deployment:** Deployed on an AWS EC2 Ubuntu instance to make the application publicly accessible.
* **Unit Testing:** Uses `unittest` to test the Flask app's functionality (ensuring that the homepage loads correctly).
* **Python 3:** The app is developed with Python 3 and uses a virtual environment for package management.

## Steps Completed:

* **Flask Web Application:**
    * Developed a simple Flask app that runs a basic homepage.
    * Configured the app to listen on all public IPs by setting `host="0.0.0.0"`.
* **EC2 Deployment:**
    * Deployed the Flask application to an Ubuntu EC2 instance.
    * Exposed the Flask app to the public via the EC2 instance's public IP address.
* **Unit Testing:**
    * Created basic unit tests using Python's `unittest` module to test the `/` route of the Flask app.
    * Ran the tests to confirm the Flask app is serving the homepage correctly with a 200 status code.

## Prerequisites:

* **AWS EC2 Instance:** An Ubuntu-based EC2 instance set up and running.
* **Python 3:** Installed on both your local machine and the EC2 instance.
* **GitHub Repository:** The Flask app and all related files are stored in a GitHub repository.

## Setup:

1.  **Clone the repository:** Clone the repository to your EC2 instance using `git clone <repository_url>`.
2.  **Install dependencies:** Navigate to the project directory on your EC2 instance and install the necessary Python dependencies using `pip install -r requirements.txt`. It is recommended to do this within a virtual environment.
3.  **Run the Flask app:** Start the Flask app on the EC2 instance using `python app.py`. Ensure the app is running on the correct port (typically 5000).
4.  **Test the app:** Run the unit tests to check if the application is functioning correctly using `python -m unittest test.py`.
