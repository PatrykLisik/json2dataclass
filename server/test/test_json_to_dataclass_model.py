from server.models.json_to_dataclass_model import JsonDictModel, JsonDictModelField


def test_simple_dict_mapping():
    data = {
        "int_key": 10,
        "float_key": 10.0,
        "str_key": "test"
    }

    mapped_model = JsonDictModel(data)
    assert len(mapped_model.fields) == 3
    assert JsonDictModelField("int_key", 10) in mapped_model.fields
    assert JsonDictModelField("float_key", 10.0) in mapped_model.fields
    assert JsonDictModelField("str_key", "test") in mapped_model.fields


def test_nested_mapping():
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

    mapped_model = JsonDictModel(data)
    assert len(mapped_model.fields) == 2
    assert "int_key" in mapped_model.fields.keys()
    assert JsonDictModelField("int_key", 1) in mapped_model.fields.values()

    nested_obj_1 = mapped_model.fields["nested_obj_1"].value
    assert len(nested_obj_1.fields) == 2
    assert "nested_int_1" in nested_obj_1.fields.keys()
    assert JsonDictModelField("nested_int_1", 2) in nested_obj_1.fields.values()

    nested_obj_2 = nested_obj_1.fields["nested_obj_2"].value
    assert len(nested_obj_2.fields) == 2
    assert "nested_int_2" in nested_obj_2.fields.keys()
    assert JsonDictModelField("nested_int_2", 3) in nested_obj_2.fields.values()

    nested_obj_3 = nested_obj_2.fields["nested_obj_3"].value
    assert len(nested_obj_3.fields) == 2
    assert JsonDictModelField("str_key", "some_str_val") in nested_obj_3.fields.values()
    assert JsonDictModelField("int_key", 4) in nested_obj_3.fields.values()


def test_list_mapping():
    data = {
        1, 2, 3, 4
    }

    mapped_model = JsonDictModel(data)
    assert len(mapped_model.fields) == 4
