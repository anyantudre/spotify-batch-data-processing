import json
from typing import Any, Dict

import requests


def get_token(client_id: str, client_secret: str, url: str) -> Dict[Any, Any]:
    """Obtain an access token using OAuth 2.0 client credentials flow

    Args:
        client_id (str): Spotify app client ID
        client_secret (str): Spotify app client secret
        url (str): Token endpoint URL

    Returns:
        Dict[Any, Any]: Dictionary containing the access token and metadata
    """
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }

    try:
        response = requests.post(url=url, headers=headers, data=payload)
        response_json = json.loads(response.content)

        return response_json

    except Exception as err:
        print(f"Error: {err}")
        return {}


def get_auth_header(access_token: str) -> Dict[str, str]:
    """Format access token as Authorization header for API requests
    
    Args:
        access_token (str): Spotify API access token
        
    Returns:
        Dict[str, str]: Authorization header dictionary
    """
    return {"Authorization": f"Bearer {access_token}"}
