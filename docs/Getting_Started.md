## FAQs
### Q: How do I run Clank locally?
**A:** Clone the repository and follow the steps in the "Getting Started" section.

### Q: Why does /simulate give an empty response?
**A:** Ensure the prompt is non-empty and parameters are set correctly. Check the logs in `logs/clank.log` for details.

### Q: Can I add my own commands?
**A:** Yes! Drop your script in the `plugins/` folder and Clank will automatically detect it.

## Step-by-Step Setup
1. **Clone the Repository**:
   Run this command in your terminal:
   ```bash
   git clone https://github.com/Eurokiwiboy/Clank.git
## Troubleshooting
- **Problem**: I get an `ImportError` when running Clank.
  **Solution**: Ensure you have Python 3.8 or later installed and that your dependencies are installed using `pip install -r requirements.txt`.

- **Problem**: My custom command doesn’t show up.
  **Solution**: Make sure the script is in the `plugins/` folder and ends with `.py`.

- **Problem**: I see an API rate limit error.
  **Solution**: Check your OpenAI API usage and increase your rate limit if needed.
