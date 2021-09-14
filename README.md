# Discover-Weekly-Archiver
https://archivediscoverweekly.com/

# Background

Every monday, Spotify will create a fresh discover playlist for you, but unless you manually save the songs there is no way to find them again. This script was designed to save your discover playlists each week into one archived playlist.

# Install 

Install relevant dependencies 
```pip install -r requirements.txt```

At the moment, you have to manually add your Spotify Access Token and update the archiver script. Instructions for generating that can be found at https://developer.spotify.com/documentation/web-api/quick-start/

You also need the correct client permissions scope to generate the token. I used ```user-read-private user-library-read user-read-email playlist-read-private playlist-modify-private playlist-modify-public```

# Running 

```python archive_dw.py```

This will create the archive playlist (if it doesn't exist) and add all your current discover songs. 

To make your life easier, it might be beneficial to run this script on a weekly schedule via a tool such as cron. 

Feel free to reach out/contribute as you see fit! Happy Discovering!  
