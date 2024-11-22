secondsInHours = 3600
secondsInMin = 60


seconds = int(input('Please Enter Seconds: '))

hours = seconds // secondsInHours
seconds = seconds % secondsInHours

minutes = seconds // secondsInMin
seconds = seconds % secondsInMin

print ('Hours: ' + str(hours) + ' Minutes: ' + str(minutes) + ' Seconds: ' + str(seconds))