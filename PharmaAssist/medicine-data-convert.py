import json

# Read medicine names from a text file
with open("excel-data.txt", "r", encoding="utf-8") as file:
    medicine_list = [line.strip() for line in file if line.strip()]  # Remove empty lines

# Convert to JSON structure
medicine_data = {"medicines": medicine_list}

# Save as JSON
with open("medicines.json", "w", encoding="utf-8") as json_file:
    json.dump(medicine_data, json_file, indent=4)

print("✅ Medicine database saved as medicines.json")
