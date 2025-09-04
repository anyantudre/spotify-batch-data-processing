from typing import Callable

import requests
from authentication import get_auth_header


def get_paginated_new_releases(
    base_url: str, access_token: str, get_token: Callable, **kwargs
) -> list:
    """Retrieve all new releases using pagination with automatic token refresh

    Args:
        base_url (str): Base URL for new releases endpoint
        access_token (str): Spotify API access token
        get_token (Callable): Function to refresh access token
        **kwargs: Additional parameters for token refresh

    Returns:
        list: List of all new release albums
    """
    headers = get_auth_header(access_token=access_token)
    request_url = base_url
    new_releases_data = []

    try:
        while request_url:
            print(f"Requesting to: {request_url}")
            response = requests.get(url=request_url, headers=headers)

            # handle token expiration (401 Unauthorized)
            if response.status_code == 401:
                token_response = get_token(**kwargs)
                if "access_token" in token_response:
                    headers = get_auth_header(
                        access_token=token_response["access_token"]
                    )
                    print("Token has been refreshed")
                    continue
                else:
                    print("Failed to refresh token.")
                    return []

            response_json = response.json()
            new_releases_data.extend(response_json["albums"]["items"])
            request_url = response_json["albums"]["next"]

        return new_releases_data

    except Exception as err:
        print(f"Error occurred during request: {err}")
        return []


def get_paginated_album_tracks(
    base_url: str,
    access_token: str,
    album_id: str,
    get_token: Callable,
    **kwargs,
) -> list:
    """Retrieve all tracks for a specific album using pagination

    Args:
        base_url (str): Base URL for albums endpoint
        access_token (str): Spotify API access token
        album_id (str): Spotify album ID
        get_token (Callable): Function to refresh access token
        **kwargs: Additional parameters for token refresh

    Returns:
        list: List of all tracks in the album
    """
    headers = get_auth_header(access_token=access_token)
    request_url = f"{base_url}/{album_id}/tracks"
    album_data = []

    try:
        while request_url:
            print(f"Requesting to: {request_url}")
            response = requests.get(url=request_url, headers=headers)
            print(f"Response status: {response.status_code}")

            # handle token expiration (401 Unauthorized)
            if response.status_code == 401:
                token_response = get_token(**kwargs)
                if "access_token" in token_response:
                    headers = get_auth_header(
                        access_token=token_response["access_token"]
                    )
                    print("Token has been refreshed")
                    continue
                else:
                    print("Failed to refresh token.")
                    return []

            response_json = response.json()
            album_data.extend(response_json["items"])
            request_url = response_json.get('next')

        return album_data

    except Exception as err:
        print(f"Error occurred during request: {err}")
        return []
