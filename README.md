# StockWatch
Flask App Development in Docker images:

Step 1: Set Up Development Environment:


Install Python and pip.

Optionally, set up a virtual environment for Python dependencies.


Step 2: Install Flask:

Install Flask using pip:

pip install flask


Step 3: Create Flask Application:

Create a new directory for your Flask project.

Create a Python file (e.g., app.py) containing your Flask application code.

Define routes, handle requests, and render templates as needed.


Step 4: Install Dependencies :
If your application has external dependencies (here, requests for API calls), install them using pip and maintain them in a requirements.txt file.
pip install requests

Dockerization:
Step 5: Create Dockerfile:

Create a Dockerfile in the root directory of your Flask project.
Define the base image, set up environment variables, copy files into the container, install dependencies, and expose necessary ports.

Step 6: Build Docker Image:
Build the Docker image using the docker build command.

docker build -t stockwatch .

Testing and Debugging:
Step 7: Run Docker Container:
Run a Docker container from the built image using the docker run command.

docker run -d -p 5000:5000 stockwatch

Step 8: Test Application:

Test the Flask application by accessing it in a web browser or using tools like curl or Postman.

Check logs using docker logs if needed.
