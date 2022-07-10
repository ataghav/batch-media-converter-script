#!/bin/bash

# this file should be copied in teh root folder of a media library and run 
# to create a playlist containting all of the files with specific type in 
# one playlist

find . -regex '.*/[^/]*.mp4' > list.m3u