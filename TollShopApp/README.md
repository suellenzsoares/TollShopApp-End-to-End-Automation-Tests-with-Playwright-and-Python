# TollShopApp - Playwright Automation Tests

This project contains automation tests for the [practicesoftwaretesting.com](https://practicesoftwaretesting.com/) website using the Playwright library with Python.

## Prerequisites

Before running the tests, make sure you have the following installed:

*   **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
*   **pip** (Python package manager): Usually comes with Python.
*   **Node.js** (required to install Playwright browsers): [Download Node.js](https://nodejs.org/en/download/)

## Environment Setup

Follow the steps below to set up the environment and run the tests:

1.  **Clone the Repository:**
    ```bash
    git clone <YOUR_REPOSITORY_URL>
    cd TollShopApp
    ```
    (Replace `<YOUR_REPOSITORY_URL>` with the actual URL of your Git repository.)

2.  **Create and Activate a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Python Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (If you don't have a `requirements.txt` yet, create one with `pip freeze > requirements.txt` after installing `playwright` and `pytest`).

4.  **Install Playwright Browsers:**
    ```bash
    playwright install
    ```

## How to Run Tests

To run all tests in the project, navigate to the `Tests` directory and use `pytest`:

```bash
cd Tests
pytest purchase_products.py
```

To run tests with headless mode disabled (to see the browser in action):

```bash
cd Tests
pytest purchase_products.py --headed
```

## Project Structure

*   `PageOjbect/`: Contains Page Object classes for interacting with web elements.
*   `Tests/`: Contains Pytest test files.
*   `requirements.txt`: List of Python dependencies.
*   `README.md`: This file.
