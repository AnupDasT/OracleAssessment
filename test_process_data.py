import pytest
from data_processor import process_data  # Adjust to your actual file name

data = """2343225,2345,us_east,RedTeam,ProjectApple,3445s
1223456,2345,us_west,BlueTeam,ProjectBanana,2211s
3244332,2346,eu_west,YellowTeam3,ProjectCarrot,4322s
1233456,2345,us_west,BlueTeam,ProjectDate,2221s
3244132,2346,eu_west,YellowTeam3,ProjectEgg,4122s"""


def test_unique_customer_ids_by_contract():
    result = process_data(data)

    # Assert for 'unique_customer_ids_by_contract'
    expected_contracts = {
        "2345": 3,
        "2346": 2,
    }
    assert result["unique_customer_ids_by_contract"] == expected_contracts, \
        "unique_customer_ids_by_contract does not match the expected result"

    print("Test Case Passed")


def test_unique_customer_ids_by_geozone():
    result = process_data(data)

    # Assert for 'unique_customer_ids_by_geozone'
    expected_geozones = {
        "us_east": 1,
        "us_west": 2,
        "eu_west": 2,
    }
    assert result["unique_customer_ids_by_geozone"] == expected_geozones, \
        "unique_customer_ids_by_geozone does not match the expected result"

    print("Test Case Passed")


def test_average_build_duration_by_geozone():
    result = process_data(data)

    # Assert for 'average_build_duration_by_geozone'
    expected_avg_durations = {
        "us_east": 3445.0,
        "us_west": 2216.0,
        "eu_west": 4222.0,
    }
    assert result["average_build_duration_by_geozone"] == expected_avg_durations, \
        "average_build_duration_by_geozone does not match the expected result"

    print("Test Case Passed")



def test_unique_customer_ids_list_by_geozone():
    result = process_data(data)

    # Assert for 'unique_customer_ids_list_by_geozone'
    expected_customer_lists = {
        "us_east": {"2343225"},
        "us_west": {"1223456", "1233456"},
        "eu_west": {"3244332", "3244132"},
    }
    assert result["unique_customer_ids_list_by_geozone"] == expected_customer_lists, \
        "unique_customer_ids_list_by_geozone does not match the expected result"

    # Additional checks for list types in unique_customer_ids_list_by_geozone
    assert isinstance(result["unique_customer_ids_list_by_geozone"]["us_east"], set), \
        "Expected a set for customer IDs list for 'us_east'"
    assert isinstance(result["unique_customer_ids_list_by_geozone"]["us_west"], set), \
        "Expected a set for customer IDs list for 'us_west'"
    assert isinstance(result["unique_customer_ids_list_by_geozone"]["eu_west"], set), \
        "Expected a set for customer IDs list for 'eu_west'"

    print("Test Case Passed")


# Verify the invalid customer IDs are failed successfully
def test_unique_invalid_customer_ids_list_by_geozone():
    result = process_data(data)

    # Assert for 'unique_invalid_customer_ids_list_by_geozone'
    expected_customer_lists = {
        "us_east": {"2343225"},
        "us_west": {"1223456", "1233456Invalid"},
        "eu_west": {"3244332", "3244132Invalid"},
    }
    assert result["unique_customer_ids_list_by_geozone"] == expected_customer_lists, \
        "unique_customer_ids_list_by_geozone does not match the expected result"

    # Additional checks for list types in unique_customer_ids_list_by_geozone
    assert isinstance(result["unique_customer_ids_list_by_geozone"]["us_east"], set), \
        "Expected a set for customer IDs list for 'us_east'"
    assert isinstance(result["unique_customer_ids_list_by_geozone"]["us_west"], set), \
        "Expected a set for customer IDs list for 'us_west'"
    assert isinstance(result["unique_customer_ids_list_by_geozone"]["eu_west"], set), \
        "Expected a set for customer IDs list for 'eu_west'"

    print("Test Case FAILED")