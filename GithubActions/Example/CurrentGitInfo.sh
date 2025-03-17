#!/bin/bash

# Get the current branch name
current_branch=$(git branch --show-current)

# Get the last commit hash
last_commit_hash=$(git rev-parse HEAD)

# Get the last commit message
last_commit_message=$(git log -1 --pretty=%B)

# Print the results
echo "Current branch: $current_branch"
echo "Last commit hash: $last_commit_hash"
echo "Last commit message: $last_commit_message"
