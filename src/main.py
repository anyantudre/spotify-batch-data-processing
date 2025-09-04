import datetime as dt
import json
import os

from dotenv import load_dotenv
from endpoint import (
    get_paginated_new_releases,
    get_paginated_album_tracks,
)
from authentication import get_token

load_dotenv(".env", override=True)

CLIENT_ID = os.getenv("CLIENT_ID", "")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")


URL_TOKEN = "https://accounts.spotify.com/api/token"
URL_NEW_RELEASES = "https://api.spotify.com/v1/browse/new-releases"
URL_ALBUM_TRACKS = "https://api.spotify.com/v1/albums"


def main():
    """Main pipeline to extract Spotify new releases and album tracks"""
    # authentication parameters
    kwargs = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "url": URL_TOKEN,
    }

    token = get_token(**kwargs)

    new_releases = get_paginated_new_releases(
        base_url=URL_NEW_RELEASES,
        access_token=token.get("access_token"),
        get_token=get_token,
        **kwargs,
    )

    print(f"New album releases have been extracted {len(new_releases)}")

    # extract album IDs from new releases
    albums_ids = [album["id"] for album in new_releases]

    print(
        f"Total number of new album releases extracted: {len(albums_ids)}"
    )

    print(f"Processing track information for each album")

    album_items = {}

    # extract track information for each album
    for album_id in albums_ids:
        album_data = get_paginated_album_tracks(
            base_url=URL_ALBUM_TRACKS,
            access_token=token.get('access_token'),
            album_id=album_id,
            get_token=get_token,
            **kwargs,
        )

        album_items[album_id] = album_data

        print(f"Album {album_id} has been processed successfully")

    # save processed data to JSON file
    if len(album_items.keys()) > 0:
        current_time = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d_%H%M%S")
        filename = f"album_items_{current_time}"

        with open(f"./{filename}.json", "w+") as albums_file:
            json.dump(album_items, albums_file, indent=2)

        print(f"Data has been saved successfully to {filename}.json")
    else:
        print(f"No data was available to be saved.")


if __name__ == "__main__":
    main()
