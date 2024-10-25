import os
import json
import pytest
from project import (
    load_json_data,
    save_json_data,
    generate_unique_random_number,
    jsonfile_empty,
    delete_item,
    add_item
)

# Run with pytest -s test_project.py
# add product name should be "test"


@pytest.fixture
def create_test_file():
    test_file = 'test_inv_file.json'
    test_data = [
        {"Name": "Test Product 1", "Price": 100, "UniqueNumber": 1234},
        {"Name": "Test Product 2", "Price": 200, "UniqueNumber": 5678}
    ]
    save_json_data(test_file, test_data)
    yield test_file
    if os.path.exists(test_file):
        os.remove(test_file)


def test_save_json_data(create_test_file):
    new_data = [{"Name": "New Product", "Price": 150, "UniqueNumber": 9999}]
    save_json_data(create_test_file, new_data)
    loaded_data = load_json_data(create_test_file)
    assert loaded_data == new_data


def test_generate_unique_random_number():
    used_numbers = [1234, 5678]
    new_number = generate_unique_random_number(used_numbers)
    assert new_number not in used_numbers


def test_jsonfile_empty():
    assert not jsonfile_empty([{"Name": "Test Product", "Price": 100}])
    assert jsonfile_empty([])


def test_delete_item(create_test_file):
    product_data = load_json_data(create_test_file)
    print("Before delete:", product_data)
    initial_count = len(product_data)
    item_id_to_delete = product_data[0]["UniqueNumber"]
    delete_item(create_test_file, product_data)
    updated_product_data = load_json_data(create_test_file)
    print("After delete:", updated_product_data)
    assert len(updated_product_data) == initial_count - 1
    assert not any(item["UniqueNumber"] == item_id_to_delete for item in updated_product_data)


def test_add_item(create_test_file):
    product_data = load_json_data(create_test_file)
    initial_count = len(product_data)
    new_product_name = "test"
    add_item(create_test_file, product_data)
    updated_product_data = load_json_data(create_test_file)
    assert len(updated_product_data) == initial_count + 1
    assert any(item["Name"] == new_product_name for item in updated_product_data)
