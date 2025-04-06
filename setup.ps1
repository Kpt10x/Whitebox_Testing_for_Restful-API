# setup.ps1 - Automate testing and coverage reporting (Windows + VS Code)

$SRC = "api/sample-api/src,genetic_testing"
$TEST = "test-suite/test_cases"
$REPORT_DIR = "coverage_reports"
$HTML_REPORT = "htmlcov/index.html"

Write-Host " Starting Enhanced White-Box Testing Workflow..."

Write-Host "`n Running unit tests only..."
python -m unittest discover -s $TEST

Write-Host "`n Running tests with coverage..."
coverage run --source=$SRC -m unittest discover -s $TEST

Write-Host "`n Generating terminal coverage report..."
coverage report -m

Write-Host "`n Generating HTML coverage report..."
coverage html

Write-Host "`n Exporting JSON coverage report..."
if (-Not (Test-Path $REPORT_DIR)) {
    New-Item -ItemType Directory -Path $REPORT_DIR | Out-Null
}
coverage json -o "$REPORT_DIR/coverage.json"

#  Check if HTML report exists before opening it
if (Test-Path $HTML_REPORT) {
    Write-Host "`n Opening HTML coverage report in browser..."
    Start-Process $HTML_REPORT
} else {
    Write-Host "`n HTML report not found. Please ensure coverage ran successfully."
}

Write-Host " Workflow completed successfully."
