# Clank Framework
A comprehensive framework for advanced structured interactions and expert ChatGPT prompting.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Getting Started](#getting-started)
4. [Commands](#commands)
5. [Use Cases](#use-cases)
6. [Contributing](#contributing)
7. [License](#license)

---

## Introduction
Clank Framework is an open-source project designed to simplify and optimise interactions with ChatGPT and other AI tools. Whether you're a developer, content creator, or AI enthusiast, Clank empowers you with modular commands, custom templates, and automation scripts to enhance AI productivity.

---

## Features
- **Modular Commands**: Customisable commands like `/simulate`, `/evaluate`, and `/compare` for varied use cases.
- **Presets**: Predefined configurations for creativity, tone, and response length.
- **Plugin Support**: Extend functionality by adding custom scripts to the `plugins/` folder.
- **Automation**: Automate repetitive tasks with robust Python scripts.
- **Community Driven**: Open for collaboration and contributions to grow the framework.

---

## Getting Started
### Prerequisites
- Python 3.8 or later
- `pip` (Python's package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Eurokiwiboy/Clank.git
   cd Clank
Install dependencies:
pip install -r requirements.txt

Run the example command:
python src/automation/simulate_command.py


## Commands
### `/simulate`
- **Description**: Simulates a prompt to test its performance.
- **Parameters**: 
  - `example_prompt`: The prompt to simulate.
  - `output_length`: Specifies the desired length of the output (e.g., "short", "detailed").
- **Example**:
  ```python
  from src.automation.simulate_command import simulate
  result = simulate("Describe the benefits of exercise.", "short")
  print(result)

/evaluate
Description: Evaluates the quality of a prompt's response.
Parameters:
prompt: The input prompt.
response: The response to evaluate.

Example:
from src.automation.evaluate_command import evaluate
evaluation = evaluate("Describe the benefits of exercise.", "Exercise improves health.")
print(evaluation)

/compare
Description: Compares the outputs of multiple prompts.
Parameters:
prompts: A list of prompts to compare.
configuration: A string specifying the configuration (e.g., "short").

from src.automation.compare_command import compare
results = compare(
    ["Describe the benefits of exercise.", "Explain AI efficiency."],
    "short"
)
print(results)
