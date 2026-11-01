import json

message = input("Paste a message to analyze: ")
lowercase_message = message.lower()

with open("scam_rules.json", "r", encoding="utf-8") as file:
    scam_rules = json.load(file)

found_warnings = []

for category, keywords in scam_rules.items():
    for word in keywords:
        if word in lowercase_message:
            found_warnings.append(category)
            print(f"Warning: {category} detected.")
            print(f"Reason: The message contains the phrase '{word}'.")
            break
risk_score = 0
with open("risk_guide.json","r",encoding="utf-8") as risk_files:
    risk_guide = json.load(risk_files)
    risk_weights = risk_guide["weights"]
for category in found_warnings:
    risk_score += risk_weights[category]

print(f"Risk score: {risk_score}/9")
if risk_score <= 2:
    risk_level = "Low"
elif risk_score <= 5:
    risk_level = "Moderate"
else:
    risk_level = "High"

print(f"Risk level: {risk_level}")

if len(found_warnings) == 0:
    print("\nNo warning signs detected by these rules.")
else:
    print(f"\nTotal warning categories detected: {len(found_warnings)}")
