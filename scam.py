message = input("Paste a message to analyze: ")
lowercase_message = message.lower()
urgency_words = [
    "urgent",
    "immediately",
    "act now",
    "expires today"
]

found_urgency = False

for word in urgency_words:
    if word in lowercase_message:
        print("\nWarning: Urgent language detected.")
        print("Reason: The message may be pressuring you to act quickly.")
        found_urgency = True
        break

if found_urgency == False:
    print("\nNo urgency-related warning signs detected.")
