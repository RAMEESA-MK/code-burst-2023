import pywhatkit as kit
import datetime
import time

# List of phone numbers to send messages to
phone_numbers = ['+919188451474', '+919072002372']

# Message to be sent
message1 = 'Hello from Python! This is a WhatsApp message sent using pywhatkit.'

message2 = 'Hello from Python! '
# Get the current time
current_time = datetime.datetime.now()
hours = current_time.hour
minutes = current_time.minute  # Send messages 2 minutes from now

# Iterate through the phone numbers and send the messages
'''for phone_number in phone_numbers:
    kit.sendwhatmsg_instantly(phone_number, message1)
    print(f"Message scheduled to {phone_number} at {hours}:{minutes}")'''


# Ask the user if they want to send the message instantly or schedule it
choice = input("Do you want to send the message instantly? (yes/no): ")

# Process the user's choice
if choice.lower() == 'yes':
    # Iterate through the phone numbers and send the messages instantly
    for phone_number in phone_numbers:
        kit.sendwhatmsg_instantly(phone_number, message1)
        time.sleep(10) 
    print("Messages sent instantly.")
else:
    
    # Iterate through the phone numbers and schedule the messages
    for phone_number in phone_numbers:
        kit.sendwhatmsg_instantly(phone_number, message2)
        time.sleep(10) 
    print("Messages sent")

    
