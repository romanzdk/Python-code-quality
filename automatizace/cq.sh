#!/usr/bin/env bash
echo "Running black";
black --check $1;

echo "Running ruff";
ruff check $1;

echo "Running mypy";
mypy $1;

echo "Running pylint";
pylint $1;