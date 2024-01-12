
# Traveling Salesman Problem Solution using Simulated Annealing

## Overview

This repository contains a Python implementation that solves the Traveling Salesman Problem (TSP) using the Simulated Annealing (SA) algorithm. It aims to find the shortest possible route that visits every city in a given list exactly once and returns to the starting city.

## Key Features

Optimized Simulated Annealing: The SA algorithm is carefully implemented to effectively explore the solution space and balance exploration and exploitation.
Clear and Concise Code: The code is well-structured, commented, and easy to understand, promoting readability and maintainability.
Flexible Input Format: Supports various input formats for city coordinates, including text files, lists, and NumPy arrays.
Visualization Capabilities: Generates a visual representation of the optimal route using the Matplotlib library (optional).
## Installation

Prerequisites:

Python 3.x
Random
Math
Matplotlib (optional, for visualization)
Installation:
Clone this repository:
Bash
git clone https://github.com/RealMehvi/Simulated-annealing-TSP.git
Use code with caution. Learn more
Install dependencies:
Bash
pip install -r requirements.txt
Use code with caution. Learn more
## Usage

Run the main script:
Bash
python SA_TSP.py
Use code with caution. Learn more
Follow the prompts to input the city coordinates and specify parameters (if desired).
## Customization

Modify the temperature_schedule function to adjust the cooling schedule of the SA algorithm.
Explore different distance calculation methods in the calculate_distance function.
Customize the visualization settings in the visualize_route function.
