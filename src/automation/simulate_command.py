def simulate(prompt, output_length="short"):
    print(f"Simulating prompt: {prompt}")
    print(f"Desired output length: {output_length}")
    # Simulated response for demonstration purposes
    response = "Exercise helps improve physical and mental health." if output_length == "short" else (
        "Exercise offers a range of benefits including improved cardiovascular health, muscle strength, mental well-being, and reduced risk of chronic diseases."
    )
    return response

# Example usage:
if __name__ == "__main__":
    simulated_response = simulate("Describe the benefits of exercise.", "short")
    print(simulated_response)
