from plyer import notification
from datetime import datetime

title = input('Enter a message title: ')
message = input('Write the message\n: ')


print('Time Format: hour:minute:second')

time = input('Enter the time for the message to be notified: ')

while True:
	if datetime.now().strftime("%H:%M:%S") == time:
		notification.notify(title=title, message=message, app_icon = 'icon.ico', app_name='Python Reminder', timeout=5)
		break
	else:
		continue