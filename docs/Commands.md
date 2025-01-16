### /simulate
- **Description**: Simulates how a prompt will execute before deployment.
- **Parameters**:
  - `example_prompt`: A sample prompt to test.
  - `output_length`: Desired length of the response (e.g., "short", "detailed").
- **Example**:
  ```json
  {
    "command": "/simulate",
    "parameters": {
      "example_prompt": "Describe the benefits of exercise.",
      "output_length": "short"
    }
  }
### /compare
- **Description**: Compares outputs of multiple prompts with the same configuration.
- **Example Usage**:compare( ["Describe the benefits of exercise.", "Explain AI efficiency."], "short" )

### /evaluate

- **Description**: The `/evaluate` command analyses the quality of a prompt's response based on predefined criteria like length, tone, and accuracy.

- **Parameters**:
  - `prompt`: The input prompt for which the response was generated.
  - `response`: The AI-generated response to the prompt.

- **Output**: A dictionary with the following keys:
  - `length`: The number of words in the response.
  - `tone`: Whether the response is "formal" or "casual".
  - `accuracy`: A placeholder indicating the evaluation of the response's correctness.

- **Example Usage**:
  ```python
  from src.automation.evaluate_command import evaluate

  prompt = "Describe the benefits of exercise."
  response = "Exercise helps improve mental and physical health."
  evaluation = evaluate(prompt, response)
  print(f"Evaluation: {evaluation}")

- **Example Output**:
{
  "length": 7,
  "tone": "casual",
  "accuracy": "High"
}
