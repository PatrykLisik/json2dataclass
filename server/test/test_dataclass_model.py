from server.models.dataclass_model import PythonDataModel


def test_simple_dict_mapping():
    data = {
        "int_key": 10,
        "float_key": 10.0,
        "str_key": "test"
    }

    mapped_model = PythonDataModel(data)
    assert len(mapped_model.data) == 1


def test_nested_dict_mapping():
    data = {
        "int_key": 1,
        "nested_obj_1": {
            "nested_int_1": 2,
            "nested_obj_2": {
                "nested_int_2": 3,
                "nested_obj_3": {
                    "str_key": "some_str_val",
                    "int_key": 4
                }
            }
        }
    }
    mapped_model = PythonDataModel(data)
    assert len(mapped_model.data) == 4


def test_homogenous_list_mapping():
    data = [1, 2, 3, 4, 5]
    mapped_model = PythonDataModel(data)
    assert len(mapped_model) == 1
