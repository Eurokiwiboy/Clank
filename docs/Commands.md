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
