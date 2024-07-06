elapsed = 3500

if elapsed < 60:
    magnitude = 'seconds'
elif elapsed < 3600:
    magnitude = 'minutes'
elif elapsed < 86400:
    magnitude = 'hours'
elif elapsed < 604800:
    magnitude = 'days'
else:
    magnitude = 'weeks'

print(magnitude)