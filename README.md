Secure Web Application Deployment with CI/CD
Project Overview

This project focuses on deploying a simple web application (Flask) on an EC2 instance using a secure connection (via HTTPS) and following DevOps best practices.
Steps Followed
1. Set Up a Simple Web Application

    A Flask web application was created as a basic app.

    The app was uploaded to GitHub and includes basic routes.

2. Launch a Cloud Server (EC2 Instance)

    An AWS EC2 instance was set up to host the Flask web app.

    Necessary packages, including Python 3, were installed.

    UFW firewall was configured to restrict unnecessary access.

3. Run Flask Application on EC2 Instance

    The Flask app was configured to run on the EC2 instance using the python3 app.py command.

    The app was initially accessible on the EC2 instance's local IP (127.0.0.1).

4. Expose the App Externally

    The Flask app was configured to accept connections from any external IP by using app.run(host='0.0.0.0', port=5000).

    The app is now accessible via the EC2 public IP.

5. Secure the Application

    ngrok was used to expose the application securely via HTTPS.

    A tunnel was created using ngrok, which allows external access to the Flask app with a secure, temporary domain.

6. Testing the Flask Application

To ensure the functionality of the Flask app, a simple test was created using Python's unittest framework. The test verifies that the home page (/) is accessible and returns a successful status code.
