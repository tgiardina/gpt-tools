#!/bin/bash

# Test 1
output=$(python3 ./unique_paths_robot.py 3 2)

if [ "$output" == "3" ]; then
    echo "Test 1 passed."
else
    echo "The result '$output' does not match expected value '3'"
fi