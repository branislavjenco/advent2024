name: Run Python Script

on:
  push:
    branches:
      - main


jobs:
  run-python:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Change to subdirectory and run script
        run: |
          cd day6
          python3 sln.py