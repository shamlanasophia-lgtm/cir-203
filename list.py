routes = [
    "Nairobi-CBD",
    "Kisumu-Central",
    "Mombasa-Port",
    "Nakuru-Town",
    "Eldoret-Center",
    "Nyeri-Market",
    "Kericho-Green",
    "Busia-Border",
    "Garissa-Town",
    "Naivasha-Lake"
]

print("Initial Routes:", routes)

# Append new route
routes.append("Malindi-Beach")

# Remove a discontinued one (example: "Busia-Border")
routes.remove("Busia-Border")

print("Updated Routes:", routes)


# Sort alphabetically
routes.sort()
print("Alphabetically Sorted:", routes)

# Reverse the list
routes.reverse()
print("Reversed Order:", routes)

count_N = sum(route.startswith("N") for route in routes)
print("Number of routes starting with 'N':", count_N)

long_routes = [route for route in routes if len(route) > 10]
print("Routes longer than 10 characters:", long_routes)
