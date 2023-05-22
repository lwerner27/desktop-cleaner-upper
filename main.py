from datetime import datetime, timedelta

def get_current_monday():
    
    # Get todays date
    today = datetime.today()
    
    if today.weekday() == 6:
        #If today is Sunday go to the next day to get the date
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
    

# TODO 
# Create function to check for the desktop directory corresponding to Monday's Date
# If the directory does not exist create it otherwise do nothing

# TODO 
# Create a function to move all files (not directories) from the desktop to the dreated directory

# TODO
# Create an optional function to compress a specified directory and remove the original 
# This function will be dependent on an arguement getting passed during execution

# Get the date for Monday of this week 
monday = get_current_monday()