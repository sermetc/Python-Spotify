#! /usr/bin/python
from Foundation import *

apple_script_code = """
set currentlyPlayingTrack to getCurrentlyPlayingTrack()
displayTrackName(currentlyPlayingTrack)

on getCurrentlyPlayingTrack()
	tell application "Spotify"
		set currentArtist to artist of current track as string
		set currentTrack to name of current track as string
		
		return currentArtist & " - " & currentTrack
	end tell
end getCurrentlyPlayingTrack

on displayTrackName(trackName)
	display notification trackName

	delay 1

end displayTrackName
"""

s = NSAppleScript.alloc().initWithSource_(apple_script_code)
s.executeAndReturnError_(None)

