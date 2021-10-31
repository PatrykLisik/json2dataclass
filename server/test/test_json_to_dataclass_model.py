from server.models.json_to_dataclass_model import JsonDictModel


def test_simple_dict_mapping():
    data = {
        "int_key_1": 10,
        "float_key": 10.0,
        "str_key": "test"
    }

    mapped_model = JsonDictModel(data)
    assert len(mapped_model.fields) == 3
