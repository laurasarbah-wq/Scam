
message = input("Paste a message to analyze: ")
lowercase_message = message.lower()

scam_rules = {
    "Urgency": ["urgent", "immediately", "act now", "expires today"],
    "Payment pressure": ["pay a fee", "send payment", "processing fee"],
    "Sensitive information": ["password", "PIN", "verification code"]
}

found_warnings = []

for category, keywords in scam_rules.items():
    for word in keywords:
        if word in lowercase_message:
            found_warnings.append(category)
            print(f"Warning: {category} detected.")
            print(f"Reason: The message contains the phrase '{word}'.")
            break

if len(found_warnings) == 0:
    print("\nNo warning signs detected by these rules.")
else:
    print(f"\nTotal warning categories detected: {len(found_warnings)}")
