#!/usr/bin/env bash
confirm() {
    if [ "$SKIP_CONFIRM" != "1" ]; then
        read -p "Press Enter/return to continue to next check ..."
    fi
}

# Check for -y or --yes flag to skip confirmations
SKIP_CONFIRM=0
for arg in "$@"
do
    case $arg in
        -y|--yes)
        SKIP_CONFIRM=1
        shift # Remove --yes or -y from processing
        ;;
        *)
        ;;
    esac
done

echo "================== LINTING (ruff) =================="
ruff fastapi tests docs_src scripts
confirm

echo "================== TYPING (mypy) =================="
mypy fastapi
confirm

echo "================== FORMATTING (black) =================="
black --check fastapi tests docs_src scripts
confirm

echo "================== FORMATTING (isort) =================="
isort --check-only fastapi tests docs_src scripts
confirm

echo "================== COMPLEXITY (cognitive) =================="
flake8 fastapi | grep Cognitive
confirm

echo "================== COMPLEXITY (cyclomatic) =================="
radon cc fastapi -sa
confirm

echo "================== DOCS (docstr-coverage) =================="
docstr-coverage -f fastapi
confirm

echo "================== SECURITY (bandit) =================="
bandit -r fastapi
confirm

echo "================== SECURITY (safety) =================="
safety check
confirm

echo "================== TESTS =================="
./scripts/test-cov-html.sh 
