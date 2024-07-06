elapsed = 7835

# Calculate hours, minutes, and seconds
# 3600 (the number of seconds in an hour)
# 60 (the number of seconds in a minute)
ju
hours = elapsed // 3600
remaining_seconds = elapsed % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")
