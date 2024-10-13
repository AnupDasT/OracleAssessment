data = """2343225,2345,us_east,RedTeam,ProjectApple,3445s
1223456,2345,us_west,BlueTeam,ProjectBanana,2211s
3244332,2346,eu_west,YellowTeam3,ProjectCarrot,4322s
1233456,2345,us_west,BlueTeam,ProjectDate,2221s
3244132,2346,eu_west,YellowTeam3,ProjectEgg,4122s"""

# Split the input data into lines
lines = data.splitlines()

# Initialize dictionaries to store results
unique_customer_ids_by_contract = {}
unique_customer_ids_by_geozone = {}
build_durations_by_geozone = {}

for line in lines:
    columns = line.split(',')
    customer_id = columns[0]
    contract_id = columns[1]
    geozone = columns[2]
    build_duration = int(columns[5][:-1])  # Remove 's' and convert to int

    # Track unique customer IDs by contract ID
    if contract_id not in unique_customer_ids_by_contract:
        unique_customer_ids_by_contract[contract_id] = set()
    unique_customer_ids_by_contract[contract_id].add(customer_id)

    # Track unique customer IDs by geozone
    if geozone not in unique_customer_ids_by_geozone:
        unique_customer_ids_by_geozone[geozone] = set()
    unique_customer_ids_by_geozone[geozone].add(customer_id)

    # Track build durations by geozone
    if geozone not in build_durations_by_geozone:
        build_durations_by_geozone[geozone] = []
    build_durations_by_geozone[geozone].append(build_duration)

# Generate report
print("Report:")

# Unique customer IDs for each contract ID
print("\nUnique customer IDs for each contract ID:")
for contract_id, customer_ids in unique_customer_ids_by_contract.items():
    print(f"Contract ID: {contract_id}, Unique Customer IDs: {len(customer_ids)}")

# Unique customer IDs for each geozone
print("\nUnique customer IDs for each geozone:")
for geozone, customer_ids in unique_customer_ids_by_geozone.items():
    print(f"Geozone: {geozone}, Unique Customer IDs: {len(customer_ids)}")

# Average build duration for each geozone
print("\nAverage build duration for each geozone:")
for geozone, durations in build_durations_by_geozone.items():
    average_duration = sum(durations) / len(durations)
    print(f"Geozone: {geozone}, Average Build Duration: {average_duration:.2f} seconds")

# List of unique customer IDs for each geozone
print("\nList of unique customer IDs for each geozone:")
for geozone, customer_ids in unique_customer_ids_by_geozone.items():
    print(f"Geozone: {geozone}, Unique Customer IDs: {customer_ids}")

