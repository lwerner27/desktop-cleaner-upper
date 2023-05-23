from datetime import datetime, timedelta
from sys import platform
import os
import getpass
import shutil

# A function to get the date for Monday of the current week. 
def get_current_monday():
    
    # Get todays date
    today = datetime.today()
    
    if today.weekday() == 6:
        # If today is Sunday go to the next day to get the date
        monday = today + timedelta(days=1)
        return "%d-%d-%d" % (monday.year, monday.month, monday.day)
    elif today.weekday() == 0:
        # If today is Monday use today's date
        monday = today
        return "%d-%d-%d" % (monday.year, monday.month, monday.day)
    else:
        # If today is after Monday go back to monday to get the date
        monday = today - timedelta(days=(today.weekday()))
        return "%d-%d-%d" % (monday.year, monday.month, monday.day)

# Function that generates the path that should be used for the desktop cleanup
def generate_desktop_path(user):
    if platform == "darwin":
        return "/Users/%s/Desktop" % user
    
# A function that creates the cleanup directory if it doesn't exist
def create_cleanup_dir(cleanup_dir):
    if not os.path.isdir(cleanup_dir):
        os.mkdir(cleanup_dir)

# A function to move all files (not directories) from the desktop to the dreated directory
def move_desktop_files(desktop_path, monday): 
    for entry in os.listdir(desktop_path):
        entry_path = os.path.join(desktop_path, entry)
        if os.path.isfile(entry_path):
            shutil.move(entry_path, os.path.join(desktop_path, monday, entry))

# TODO
# Create an optional function to compress a specified directory and remove the original 
# This function will be dependent on an arguement getting passed during execution

# Get the date for Monday of this week 
monday = get_current_monday()

# Generate the path for the cleanup directory
desktop_path = generate_desktop_path(getpass.getuser())

# Create the clean up directory if it does not exist
create_cleanup_dir(os.path.join(desktop_path, monday))

# Moves files (not directories) to the directory for the current week
move_desktop_files(desktop_path, monday)