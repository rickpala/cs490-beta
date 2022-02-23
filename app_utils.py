from typing import List, Dict
# Utility functions for this project.

# Constants
BACKEND_URL = "https://cs100-testing-backend.herokuapp.com"
COOKIE_ROLE = "Role"

def keys_missing(req_keys: List[str], data: Dict) -> bool:
    """Returns true if any keys are missing from data."""
    if not isinstance(req_keys, List):
        return False
    if len(req_keys) != len(data):
        return False
    return not all(key in data for key in req_keys)
