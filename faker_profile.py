import csv
from faker import Faker
from mimesis import Generic

fake = Faker()
generic = Generic()

# Generate data as shown in the previous code snippet

from faker import Faker
from mimesis import Generic

fake = Faker()
generic = Generic()

# Generate personal information
name = fake.name()
age = fake.random_int(min=18, max=65)
gender = fake.random_element(["Male", "Female"])
nationality = generic.nationality()
language_preferences = [generic.language_name() for _ in range(fake.random_int(min=1, max=3))]

# Generate interests
outdoor_activities = [generic.activity() for _ in range(fake.random_int(min=1, max=5))]
art_and_culture = [generic.artwork() for _ in range(fake.random_int(min=1, max=5))]
history = [generic.historical_event() for _ in range(fake.random_int(min=1, max=5))]
food_and_dining = [generic.food() for _ in range(fake.random_int(min=1, max=5))]
shopping = [generic.product() for _ in range(fake.random_int(min=1, max=5))]
nightlife_and_entertainment = [generic.entertainment() for _ in range(fake.random_int(min=1, max=5))]
wildlife_and_nature = [generic.animal() for _ in range(fake.random_int(min=1, max=5))]
sports = [generic.sport() for _ in range(fake.random_int(min=1, max=5))]

# Generate travel style
travel_styles = generic.travel_type().split(', ')

# Generate previous travel experiences
countries_visited = [generic.country() for _ in range(fake.random_int(min=1, max=5))]
favorite_destinations = [generic.city() for _ in range(fake.random_int(min=1, max=5))]
activities_enjoyed = [generic.activity() for _ in range(fake.random_int(min=1, max=5))]

# Generate accommodation preferences
accommodation_preferences = generic.accommodation_type().split(', ')

# Generate dietary restrictions
dietary_restrictions = generic.diet().split(', ')

# Generate transportation preferences
transportation_preferences = generic.transport().split(', ')

# Generate accessibility needs
accessibility_needs = generic.accessibility().split(', ')

# Generate notification preferences
frequency_preferences = generic.frequency().split(', ')
communication_channels = generic.communication().split(', ')

# Print the generated data
print("Personal Information:")
print("Name:", name)
print("Age:", age)
print("Gender:", gender)
print("Nationality:", nationality)
print("Language Preferences:", language_preferences)

print("\nInterests:")
print("Outdoor Activities:", outdoor_activities)
print("Art and Culture:", art_and_culture)
print("History:", history)
print("Food and Dining:", food_and_dining)
print("Shopping:", shopping)
print("Nightlife and Entertainment:", nightlife_and_entertainment)
print("Wildlife and Nature:", wildlife_and_nature)
print("Sports:", sports)

print("\nTravel Style:")
print("Travel Styles:", travel_styles)

print("\nPrevious Travel Experiences:")
print("Countries Visited:", countries_visited)
print("Favorite Destinations:", favorite_destinations)
print("Activities Enjoyed:", activities_enjoyed)

print("\nAccommodation Preferences:")
print("Accommodation Preferences:", accommodation_preferences)

print("\nDietary Restrictions:")
print("Dietary Restrictions:", dietary_restrictions)

print("\nTransportation Preferences:")
print("Transportation Preferences:", transportation_preferences)

print("\nAccessibility Needs:")
print("Accessibility Needs:", accessibility_needs)

print("\nNotification Preferences:")
print("Frequency Preferences:", frequency_preferences)
print("Communication Channels:", communication_channels)

# Create a list of dictionaries to store the data
data = [
    {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Nationality": nationality,
        "Language Preferences": ", ".join(language_preferences),
        "Outdoor Activities": ", ".join(outdoor_activities),
        "Art and Culture": ", ".join(art_and_culture),
        "History": ", ".join(history),
        "Food and Dining": ", ".join(food_and_dining),
        "Shopping": ", ".join(shopping),
        "Nightlife and Entertainment": ", ".join(nightlife_and_entertainment),
        "Wildlife and Nature": ", ".join(wildlife_and_nature),
        "Sports": ", ".join(sports),
        "Travel Styles": ", ".join(travel_styles),
        "Countries Visited": ", ".join(countries_visited),
        "Favorite Destinations": ", ".join(favorite_destinations),
        "Activities Enjoyed": ", ".join(activities_enjoyed),
        "Accommodation Preferences": ", ".join(accommodation_preferences),
        "Dietary Restrictions": ", ".join(dietary_restrictions),
        "Transportation Preferences": ", ".join(transportation_preferences),
        "Accessibility Needs": ", ".join(accessibility_needs),
        "Frequency Preferences": ", ".join(frequency_preferences),
        "Communication Channels": ", ".join(communication_channels)
    }
]

# Specify the CSV file path
csv_file = "tourist_data.csv"

# Write the data to the CSV file
fieldnames = data[0].keys()

with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print("Data saved successfully to", csv_file)
