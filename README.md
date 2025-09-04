# Spotify Batch Data Processing

A simple Python project for extracting and processing data from the Spotify Web API in batch operations. This demonstrates API authentication, pagination techniques, and serves as a foundation for potential future music analytics projects, trend analysis/clustering, or music recommendation algorithms.


### Functionality
- **OAuth 2.0 Authentication**: token-based authentication with automatic refresh
- **Paginated Data Retrieval**: two pagination strategies (offset-based and URL-based)
- **Rate Limit Handling**: built-in rate limiting awareness and best practices


### API Endpoints Utilized
- [Browse New Releases](https://developer.spotify.com/documentation/web-api/reference/get-new-releases)
- [Get Album Tracks](https://developer.spotify.com/documentation/web-api/reference/get-an-albums-tracks)


### Spotify App Setup
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/)
2. Create a new app with these settings:
   - **App name**: `spotify-batch-processing`
   - **App description**: `Batch data processing from Spotify API`
   - **Redirect URIs**: `http://127.0.0.1:3000`
   - **API**: Web API

3. Copy `Client ID` and `Client Secret`


### Environment config
Create a file `src/.env` with your Spotify credentials:
```
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
```

- Installation
```bash
# clone repo
git clone https://github.com/anyantudre/spotify-batch-data-processing.git
cd spotify-batch-data-processing

# deps
pip install requests python-dotenv spotipy
```

- Run the app
```bash
python src/main.py
```


### Pagination
We implemented two pagination approaches:
1. Offset-Based Pagination
    - Manually calculates next page using `offset` + `limit`
    - More control over pagination logic
    - Useful for custom pagination requirements

2. URL-Based Pagination  
    - Uses the `next` URL provided by the API
    - Simpler implementation
    - Recommended approach for most use cases


### Rate limiting
Spotify API uses dynamic rate limiting based on a rolling 30-second window. We include:  
- **Built-in delays**: configurable request intervals
- **Best practices**: exponential backoff strategies
- **Monitoring**: request timing analysis


### Future enhancements
1. Data & Analytics
    - Audio features integration (tempo, energy, danceability)
    - Advanced filtering and artist analytics
    - Data visualization dashboards

2. Technical
    - Database integration (PostgreSQL/MongoDB)
    - Async processing and caching
    - Docker containerization
    - CI/CD pipeline

3. Machine Learning
    - Music recommendation algorithms
    - Genre classification models
    - Trend analysis and clustering
