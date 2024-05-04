# StockWatch
**Flask App Development in Docker images:**

**Step 1:** Set Up Development Environment:


Install Python and pip.

Optionally, set up a virtual environment for Python dependencies.


**Step 2:** Install Flask:

Install Flask using pip:

pip install flask


**Step 3:** Create Flask Application:

Create a new directory for your Flask project.

Create a Python file (e.g., app.py) containing your Flask application code.

Fetching Stock Prices:

Created a function (get_stock_prices()) to fetch stock prices from the Polygon.io API.

Constructed the API URL using the user-provided stock symbol, start date, and end date.

Sent a GET request to the Polygon.io API using the requests.get() function.


**Step 4:** Install Dependencies :
If your application has external dependencies (here, requests for API calls), install them using pip and maintain them in a requirements.txt file.
pip install requests

**Dockerization:**
Step 5: Create Dockerfile:

Create a Dockerfile in the root directory of your Flask project.
Define the base image, set up environment variables, copy files into the container, install dependencies, and expose necessary ports.

**Step 6:** Build Docker Image:
Build the Docker image using the docker build command.

docker build -t stockwatch .

**Testing and Debugging:**
Step 7: Run Docker Container:
Run a Docker container from the built image using the docker run command.

docker run -d -p 5000:5000 stockwatch

Step 8: Test Application:

Test the Flask application by accessing it in a web browser or using tools like curl or Postman.

Check logs using docker logs if needed.
