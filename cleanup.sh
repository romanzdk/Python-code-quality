#!/usr/bin/env bash
rm -rf _* docs .pytest_cache .ruff_cache .scannerwork .coverage *.lprof *profile* *.png .nox .mypy_cache *.so index.rst make.bat;
find . -type f -name "*.so" -exec rm {} +;
find . -type d -name __pycache__ -exec rm -rf {} +
find . -type d -name target -exec rm -rf {} +
find . -type d -name build -exec rm -rf {} +
