# 🔍 Enhanced White-Box Testing for RESTful APIs using Search-Based Methods

This project demonstrates enhanced white-box testing strategies for RESTful APIs, integrating dynamic testing (using `unittest` + `hypothesis`) and **search-based test case generation** via **genetic algorithms** (`pygad`).

---

## 🗂 Project Structure

Enhanced-WhiteBox-Testing/ │ ├── api/ │ └── sample-api/ │ └── src/ │ └── app.py # Flask API source │ ├── genetic_testing/ │ └── genetic_test_gen.py # Genetic algorithm-based test case generator │ ├── test-suite/ │ └── test_cases/ │ ├── test_api.py # Dynamic tests using unittest + hypothesis │ └── test_genetic.py # Validation for genetic algorithm logic │ ├── coverage_reports/ │ └── coverage.json # Coverage output (generated) │ ├── htmlcov/ # Coverage HTML report (auto-generated) │ ├── setup.ps1 # PowerShell script to automate testing + reporting (Windows) ├── Makefile # (Optional) Makefile for UNIX-based automation └── README.md # You're here!

---

## 🚀 Quick Start

### 1. 📦 Install Dependencies

bash
pip install -r requirements.txt

### 2. Start the API

        From the root folder:

                python api/sample-api/src/app.py
        Leave this terminal open. The API will run at:
        http://127.0.0.1:5000

### 3. 🧪 Run Tests (in a new terminal)

    python -m unittest discover -s test-suite/test_cases

### 4. 🧬 Run Genetic Test Generator (Optional)

    python genetic_testing/genetic_test_gen.py

### 5. 📈 Generate Coverage Report

    coverage run --source=api/sample-api/src -m unittest discover -s test-suite/test_cases
    coverage report -m
    coverage html

    Then open the HTML coverage report:

    start htmlcov/index.html

    OR just use:

    .\setup.ps1


📎 Notes

    Make sure your Flask API is running on http://localhost:5000

    The GA will interact with the /users POST endpoint

    Coverage includes both white-box API logic and test generation code


---

```powershell
# setup.ps1 - Automates testing & coverage for API and Genetic Test Code

Write-Host "📌 Running Unit Tests with Coverage..."

# Step 1: Run coverage
coverage run --source=api/sample-api/src,genetic_testing -m unittest discover -s test-suite/test_cases

# Step 2: Show summary in terminal
coverage report -m

# Step 3: Generate HTML coverage
coverage html

# Step 4: Generate JSON report
coverage json -o coverage_reports/coverage.json

# Step 5: Open HTML report in browser
Start-Process "$PWD/htmlcov/index.html"

Write-Host "`n All tests complete. Reports generated successfully."
