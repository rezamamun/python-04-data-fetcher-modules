from datetime import datetime

# Get the current date and time, then format it as "YYYY-MM-DD HH:MM:SS".
now = datetime.now()
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")

print(f"Current Date and Time: {formatted_now}")
