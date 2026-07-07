# Inventory Management System

This is a simple Inventory System built with python and flask.
It allows the user to view inventory items, update exicting items, delete and import product information using the OpenFoodFacts API.

## Features

- View all inventory items
- View one inventory item by ID
- Add a new inventory item
- Update an existing inventory item
- Delete an inventory item
- Search for a product using a barcode
- Import product details from OpenFoodFacts
- Run tests using pytest

## Project Structure

```text
Inventory_Management_System/
├── App/
│   ├── App.py
│   ├── External_API.py
│   ├── data.py
│   └── __init__.py
├── test/
│   ├── test_App.py
│   ├── test_external_api.py
│   └── __init__.py
├── CLI.py
├── README.md
└── requirements.txt
```

## Requirements

- Python 3
- Flask
- requests
- pytest

Install the requirements with:

```bash
pip install -r requirements.txt


To Run The Flask API

From the project folder, run:

```bash
python -m App.App
```

The API will run at:

```text
http://127.0.0.1:5000