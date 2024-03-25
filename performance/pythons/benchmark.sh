#!/usr/bin/env bash

# Define benchmark scripts
declare -a benchmarks=("fib.py" "data.py" "io.py" "cpu.py" "concurrency.py" "mandelbrot.py")

# Define Python versions
declare -a py_versions=("python3.10" "python3.11" "python3.12")

# Run benchmarks
for benchmark in "${benchmarks[@]}"; do
    echo "Running $benchmark..."
    for version in "${py_versions[@]}"; do
        echo "Using $version"
        start_time=$(date +%s) # Capture start time in seconds
        pyenv exec $version "performance/pythons/$benchmark"
        end_time=$(date +%s) # Capture end time in seconds
        duration=$((end_time - start_time)) # Calculate duration in seconds
        echo "Time taken by $version: $duration seconds"
    done
    echo "-----------------------------------"
done