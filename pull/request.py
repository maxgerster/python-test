import requests
import warnings
import re

def request(URL):

    # Disable warnings
    warnings.filterwarnings("ignore")

    # Get JSON from URL
    response = requests.get(URL, verify=False).json()

    # Regex on JSON
    formatted_response = re.sub('...', '...', str(response))

    # Return
    return formatted_response
