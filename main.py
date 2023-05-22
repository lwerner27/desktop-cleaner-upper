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

# Get the date for Monday of this week 
monday = get_current_monday()