#! /usr/bin/python
from subprocess import Popen
from sys import platform

if platform == "darwin":
	p = Popen(['osascript', '/Users/sermet/Desktop/work/github/Python-Spotify/MacOS/script.scpt'])
