def process_data(data):
    # Your original code goes here
    lines = data.splitlines()
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

    report = {
        "unique_customer_ids_by_contract": {contract_id: len(customer_ids) for contract_id, customer_ids in unique_customer_ids_by_contract.items()},
        "unique_customer_ids_by_geozone": {geozone: len(customer_ids) for geozone, customer_ids in unique_customer_ids_by_geozone.items()},
        "average_build_duration_by_geozone": {geozone: sum(durations) / len(durations) for geozone, durations in build_durations_by_geozone.items()},
        "unique_customer_ids_list_by_geozone": unique_customer_ids_by_geozone,
    }

    return report
