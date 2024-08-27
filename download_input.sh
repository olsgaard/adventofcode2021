#!/bin/bash

# Check if the script was provided with a day number as an argument
if [ $# -eq 1 ]; then
  year_number="$1"
  first=1
  last=25
elif [ $# -eq 2 ]; then
  year_number="$1"
  first="$2"
  last="$2"
else
  echo "Usage: $0 <year> [<day_number>]"
  exit 1
fi

mkdir "$year_number"

# Check if the "sessionId" file exists
if [ ! -f "sessionId.key" ]; then
  echo "Error: The 'sessionId.key' file does not exist."
  echo "Please log in to adventofcode.com and save the value of your session cookie to 'sessionId.key'"
  exit 1
fi

# Use curl to download the puzzle input with the session ID as a cookie
for day_number in $(seq "$first" "$last"); do
  url="https://adventofcode.com/${year_number}/day/${day_number}/input"
  curl "$url" \
    --cookie "session=$(<sessionId.key)" \
    -o "${year_number}/day${day_number}_input.txt"

  # Check the exit status to determine if the download was successful
  if [ $? -eq 0 ]; then
    echo "Puzzle input for Day $day_number downloaded successfully!"
  else
    echo "Failed to download puzzle input for Day $day_number."
  fi
done
