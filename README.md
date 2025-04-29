# Secure Web Application Deployment with Flask

This project demonstrates the deployment of a basic Flask web application on an AWS EC2 instance. The web application is designed to be publicly accessible and incorporates basic security measures, along with testing using Python's `unittest` framework to ensure proper functionality.

## Key Features:

* **Flask Web Application:** A simple Flask app that serves a basic homepage.
* **EC2 Deployment:** Deployed on an AWS EC2 Ubuntu instance to make the application publicly accessible.
* **Unit Testing:** Uses `unittest` to test the Flask app's functionality (ensuring that the homepage loads correctly).
* **Python 3:** The app is developed with Python 3 and uses a virtual environment for package management.
* **Basic Security Measures:** Implements fundamental security practices for the deployed application.

## Steps Completed:

* **Flask Web Application:**
    * Developed a simple Flask app that runs a basic homepage.
    * Configured the app to listen on all public IPs by setting `host="0.0.0.0"`.
* **EC2 Deployment:**
    * Deployed the Flask application to an Ubuntu EC2 instance.
    * Exposed the Flask app to the public via the EC2 instance's public IP address (initially through a temporary HTTPS tunnel).
* **Unit Testing:**
    * Created basic unit tests using Python's `unittest` module to test the `/` route of the Flask app.
    * Ran the tests to confirm the Flask app is serving the homepage correctly with a 200 status code.
* **Basic Security Measures:**
    * **Hosted on a Secure EC2 Instance:** The Flask app was deployed on an AWS EC2 instance with a key pair (`.pem` file) for secure SSH access.
    * **Controlled Inbound Traffic:** Only specific ports (such as SSH `22` and app port `5000`) were opened in the EC2 instance’s security group to minimize exposure.
    * **Server Firewall Configuration with UFW:** The server used UFW (Uncomplicated Firewall) to allow only necessary ports (like `22` for SSH and `5000` for the app) and block all other incoming connections by default.
    * **Temporary HTTPS Access Using ngrok:** To expose the Flask app publicly, `ngrok` was used to create a secure HTTPS tunnel to the application. This allowed encrypted access to the app during testing without manually setting up an SSL certificate.
    * **Localhost Binding:** The Flask app was configured to run on `0.0.0.0`, making it reachable externally but still protected by firewall and network settings.
    * **Environment Isolation:** The app and its dependencies were installed inside the EC2 environment, avoiding conflicts with global system packages.

## Prerequisites:

* **AWS EC2 Instance:** An Ubuntu-based EC2 instance set up and running.
* **Python 3:** Installed on both your local machine and the EC2 instance.
* **GitHub Repository:** The Flask app and all related files are stored in a GitHub repository.
* **ngrok:** Installed and configured on your local machine or the EC2 instance if you intend to use it for temporary public access.

## Setup:

1.  **Clone the repository:** Clone the repository to your EC2 instance using `git clone <repository_url>`.
2.  **Install dependencies:** Navigate to the project directory on your EC2 instance and install the necessary Python dependencies using `pip install -r requirements.txt`. It is recommended to do this within a virtual environment.
3.  **Configure Firewall (UFW):** Ensure UFW is enabled and configured to allow SSH (port `22`) and the Flask app's port (port `5000` by default). You can check the status with `sudo ufw status` and add rules with `sudo ufw allow <port>`.
4.  **Run the Flask app:** Start the Flask app on the EC2 instance using `python app.py`. Ensure the app is running on the correct port (typically 5000).
5.  **(Optional) Expose via ngrok:** If you need temporary public HTTPS access, run `ngrok http 5000` on your EC2 instance or your local machine (if tunneling to the EC2 instance).
6.  **Test the app:** Run the unit tests to check if the application is functioning correctly using `python -m unittest tests.py`.
