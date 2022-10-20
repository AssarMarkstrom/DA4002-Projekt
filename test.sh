#!/bin/env bash

for i in test_*.py; do
        echo "Running $i"
        python3 -m unittest $i
done
