# TollShopApp-End-to-End-Automation-Tests-with-Playwright-and-Python
This repository contains a suite of end-to-end automation tests for an e-commerce application, built using Playwright with Python and Pytest. It demonstrates robust testing practices, including the Page Object Model (POM) for maintainable and scalable test automation.
# TollShopApp - Playwright Automation Tests

This project contains automation tests for the [practicesoftwaretesting.com](https://practicesoftwaretesting.com/) website using the Playwright library with Python.

## Prerequisites

Before running the tests, make sure you have the following installed:

*   **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
*   **pip** (Python package manager): Usually comes with Python.
*   **Node.js** (required to install Playwright browsers): [Download Node.js](https://nodejs.org/en/download/)

## Environment Variables

Sensitive information like `BASE_URL`, `USER_EMAIL`, and `USER_PASSWORD` are stored in a `.env` file. This file is located in the `TollShopApp/` directory.

**How to create the `.env` file:**
1.  Navigate to the `TollShopApp/` directory.
2.  Create a new file named `.env`.
3.  Add the following content to the `.env` file:

```
BASE_URL=https://practicesoftwaretesting.com/
USER_EMAIL=customer2@practicesoftwaretesting.com
USER_PASSWORD=welcome01
CARD_NUMBER=0000-0000-0000-0000
CARD_EXPIRY=10/2028
CARD_CVV=123
CARD_NAME=Jack Howe
```
IMPORTANT NOTICE: The data used in this example is fictitious and intended solely for testing purposes. It is crucial that when replicating this process, you use test data and do not insert or share real or confidential information.

Example `.env` file:
```
BASE_URL=https://practicesoftwaretesting.com/
USER_EMAIL=test@example.com
USER_PASSWORD=password123
```

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
    (The `requirements.txt` file now includes `python-dotenv` for loading environment variables.)

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

**Note on Test Setup:** For a larger test suite, it would be beneficial to configure Pytest fixtures (e.g., in a `conftest.py` file) to handle browser setup and teardown, as well as Page Object instantiation. However, for the purpose of demonstrating this single test, these steps are handled directly within the `test_purchase_products` function.

To run tests with headless mode disabled (to see the browser in action):

```bash
cd Tests
pytest purchase_products.py --headed
```

## Continuous Integration (CI)

This repository includes a GitHub Actions workflow file (`.github/workflows/ci.yml`) that automatically installs dependencies and runs the Playwright + Pytest tests on every push or pull request. Environment variables required for the tests are configured directly in the workflow file for CI execution. You can customize this workflow to fit your team's needs.

## Project Structure

*   `PageOjbect/`: Contains Page Object classes for interacting with web elements.
*   `Tests/`: Contains Pytest test files.
*   `requirements.txt`: List of Python dependencies.
*   `.env`: Environment variables for sensitive data
*   `README.md`: This file.
