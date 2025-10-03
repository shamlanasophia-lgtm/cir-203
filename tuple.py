# Create a tuple for a patient
patient = ("jijo", 45, "120/80 mmHg", 72)

print("Patient Record:", patient)

# Access age (index 1) and heart rate (index 3)
age = patient[1]
heart_rate = patient[3]

print("Patient Age:", age)
print("Patient Heart Rate:", heart_rate)

# Original patient tuple
patient = ("John Doe", 45, "120/80 mmHg", 72)

# Step 1: Convert to list
patient_list = list(patient)

# Step 2: Update the heart rate (index 3)
patient_list[3] = 80   # new heart rate

# Step 3: Convert back to tuple
patient = tuple(patient_list)

print("Updated Patient Record:", patient)

# Create a tuple of 5 patients (Name, Age, Blood Pressure, Heart Rate)
patients = (
    ("John Doe", 35, "120/80", 72),
    ("Alice Smith", 40, "130/85", 76),
    ("Robert Brown", 29, "110/70", 68),
    ("Mary Johnson", 50, "140/90", 80),
    ("James Wilson", 60, "135/88", 75)
)

# Extract all names
names = [patient[0] for patient in patients]

# Print names
print("Patient Names:", names)
