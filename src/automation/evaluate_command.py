def evaluate(prompt, response):
    evaluation = {
        "length": len(response.split()),
        "tone": "formal" if "you are" in response else "casual",
        "accuracy": "High"  # Placeholder for advanced logic
    }
    return evaluation

# Example usage
if __name__ == "__main__":
    prompt = "Describe the benefits of exercise."
    response = "Exercise helps improve mental and physical health."
    evaluation = evaluate(prompt, response)
    print(f"Evaluation: {evaluation}")
