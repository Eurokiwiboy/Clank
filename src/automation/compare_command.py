def compare(prompts, configuration):
    results = {}
    for prompt in prompts:
        results[prompt] = simulate(prompt, configuration)
    return results

# Example usage
if __name__ == "__main__":
    prompts = [
        "Describe the benefits of exercise.",
        "Explain how AI improves efficiency."
    ]
    config = "short"
    outputs = compare(prompts, config)
    for prompt, result in outputs.items():
        print(f"Prompt: {prompt}\nOutput: {result}\n")
