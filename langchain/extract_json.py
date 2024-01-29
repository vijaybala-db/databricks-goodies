import re
import json

def extract_json(text):
    # Regex pattern to find a JSON object
    # This pattern looks for the curly braces and everything in between
    pattern = r'\{.*\}'

    # Search for the pattern in the text
    match = re.search(pattern, text, re.DOTALL)

    # If a match is found, return it as a JSON object
    if match:
        try:
            # Parse the matched string into a JSON object
            json_object = json.loads(match.group())
            return json_object
        except json.JSONDecodeError:
            # Handle case where the matched string is not valid JSON
            return "Found text is not a valid JSON object."
    else:
        return "No JSON object found in the text."

if __name__ == '__main__':
    # Example usage
    input_text = """
    Here are the nutrition facts for a single avocado:

    {
    "calories": 255,
    "fat": 21.0,
    "carbohydrates": 14.0,
    "sodium": 1.0
    }
    """

    extracted_json = extract_json(input_text)
    print(extracted_json)
