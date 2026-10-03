# Python Assignment 04 — Data Fetcher Modules

A small collection of beginner Python console programs demonstrating the standard `datetime` and `json` modules.

## Project Description

This repository contains two standalone Python programs:

1. **Current Date and Time** — Uses the `datetime` module to fetch and display the current date and time.
2. **Student to JSON** — Builds a student dictionary and converts it into a JSON string using the `json` module.

## Features

### Current Date and Time (`problem1.py`)
- Uses `datetime.now()` to get the current date and time.
- Formats it as `YYYY-MM-DD HH:MM:SS`.
- Prints the formatted date and time.

### Student to JSON (`problem2.py`)
- Defines a student dictionary with `name`, `age`, and `department`.
- Converts the dictionary into a JSON string using `json.dumps()`.
- Prints the resulting JSON string.

## Technologies Used

- Python 3
- `datetime` module (standard library)
- `json` module (standard library)

## Setup / Run Instructions

1. Make sure Python 3 is installed:
   ```bash
   python --version
   ```
2. Clone this repository:
   ```bash
   git clone <repository-url>
   cd python-04-data-fetcher-modules
   ```
3. Run the Current Date and Time program:
   ```bash
   python problem1.py
   ```
4. Run the Student to JSON program:
   ```bash
   python problem2.py
   ```

## Example Output

### Current Date and Time
```
Current Date and Time: 2026-09-30 11:30:45
```

### Student to JSON
```
{"name": "Rahim", "age": 20, "department": "CSE"}
```
