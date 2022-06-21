# Spotify Seach Script - Python

## Running the Script:
- Check if current directory is where you have downloaded the script file
- On the basis of your python version installed, use one the command "python spotify_search_script.py" or "python3 spotify_search_script.py" to run the script
- That's it. No follow the flow in the script.


## Assumptions
- "Artist Name": As spotify allow alphabets, digits and special characters in the artist name, we have not put constraint on artist_name in our script. We have only put the check that artist name can't be empty.
- "Country": While fetching top tracks for an artist using "/artists/{id}/top-tracks/", we have to specify the country by passing "market" parameter. We have used INDIA ("market=IN") for all.
- "No Artists": When user enters artist name which is not available, we are exiting the program by displaying message - "Oh ho! No Artist found by this name." "Spotify Search will close now. Bbye!"
- "No Tracks": When the entered artist is having no tracks available, we are exiting the program by displaying message - "Oh ho! This Artist does not have any tracks." "Spotify Search will close now. Bbye!"
