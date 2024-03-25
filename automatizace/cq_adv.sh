#!/usr/bin/env bash

# Function to run tools on specified paths or the current directory
run_tools() {
    local check_mode=1 # By default, run in check mode
    local paths=()    # Array to store paths

    # Parse arguments
    for arg in "$@"; do
        if [ "$arg" = "--fix" ]; then
            check_mode=0 # Disable check mode if --fix is present
        else
            paths+=("$arg") # Add non-flag arguments to paths array
        fi
    done

    # If no paths are provided, use the current directory
    if [ ${#paths[@]} -eq 0 ]; then
        paths=(".")
    fi

    # Configure flags for isort and black based on check mode
    local isort_flags=""
    local black_flags=""
    if [ $check_mode -eq 1 ]; then
        isort_flags="--check-only"
        black_flags="--check"
    fi

    # Running isort
    echo "Running isort..."
    isort $isort_flags "${paths[@]}"

    # Running black
    echo "Running black..."
    black $black_flags "${paths[@]}"

    # Running mypy
    echo "Running mypy..."
    mypy "${paths[@]}"

    # Running pylint
    echo "Running pylint..."
    for path in "${paths[@]}"; do
        pylint "$path"
    done
}

# Run the tools with provided arguments or in the current directory
run_tools "$@"
