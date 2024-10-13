#write a code to validate the api resonse from a sample website
import requests

def validate_api_response(url):
    """
    Validates the API response from the given URL.

    Args:
        url (str): The URL of the API endpoint.

    Returns:
        bool: True if the API response is valid, False otherwise.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return False

# Example usage
api_url = "https://api.example.com/data"
is_valid = validate_api_response(api_url)
print(f"API response is valid: {is_valid}")


