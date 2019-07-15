import sys
import json
import os
import spotipy
import spotipy.util as util


ARCHIVE_PLAYLIST_NAME = "(Archived) Discover Weekly"
ARCHIVE_PLAYLIST_DESCRIPTION = "A playlist containing past discover weekly playlists"

#INSERT SPOTIFY ACCESS TOKEN HERE#
ACCESS_TOKEN = ''

if ACCESS_TOKEN == '':
    print("Please insert spotify access token here. Relevant documentation can be found on Spotify's Developer Page: https://developer.spotify.com/documentation/web-api/quick-start/")
    exit(-1)

SPOTIFY_CLIENT = spotipy.Spotify(auth=ACCESS_TOKEN)
USERNAME = SPOTIFY_CLIENT.current_user()['id']

#fetches dw playlist - returns a list of ids  
def get_discover_weekly(client):

    playlists = client.current_user_playlists()["items"]
    dw_tracks = [] 

    for playlist in playlists:
        name = playlist["name"]


        if name == "Discover Weekly":
            dw_id = playlist["id"]
            
            dw = client.user_playlist(USERNAME, dw_id, fields="tracks,next")
            tracks = dw['tracks']

            for track_data in tracks["items"]:
                track_id = track_data["track"]["id"]
                dw_tracks.append(track_id)

    
    return dw_tracks

#attempts to add current dw playlist to archive playlist, creates archive if not
def archive_discover_weekly(client): 
    dw_tracks = get_discover_weekly(client)
    archive_id = None 
    
    playlists = client.current_user_playlists()["items"]

    for playlist in playlists:
        name = playlist["name"] 

        if name == ARCHIVE_PLAYLIST_NAME:
            archive_id = playlist["id"]
            break

    if not archive_id:
        #TODO: check for duplicate songs
        #TODO: figure out keyword error when passing description..?
        archive_playlist = client.user_playlist_create(USERNAME, ARCHIVE_PLAYLIST_NAME)
        archive_id = archive_playlist["id"]
    
    client.user_playlist_add_tracks(USERNAME, archive_id, dw_tracks)            

    return ""


if __name__ == '__main__':
    archive_discover_weekly(SPOTIFY_CLIENT)
