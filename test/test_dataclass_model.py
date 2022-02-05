from json2dataclass.models.dataclass_model import PythonDataModel


def test_simple_dict_mapping():
    data = {
        "int_key": 10,
        "float_key": 10.0,
        "str_key": "test"
    }

    mapped_model = PythonDataModel(data)
    assert len(mapped_model.data) == 1

    generate_code = mapped_model.generate_code()
    exec(generate_code, globals(), globals())


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

    generate_code = mapped_model.generate_code()
    exec(generate_code, globals(), globals())


def test_homogenous_list_mapping():
    data = [1, 2, 3, 4, 5]
    mapped_model = PythonDataModel(data)
    assert len(mapped_model.data) == 1
    list_class = mapped_model.data.pop()
    assert list_class.fields.pop().type_name == "list[int]"

    generate_code = mapped_model.generate_code()
    exec(generate_code, globals(), globals())


def test_list_of_heterogeneous_primitive_types():
    data = [1, "aaa", 3.0, 4.5, 5, "banana"]
    mapped_model = PythonDataModel(data)
    assert len(mapped_model.data) == 1
    list_class = mapped_model.data.pop()
    assert list_class.fields.pop().type_name.startswith("list[Union[")

    generate_code = mapped_model.generate_code()
    exec(generate_code, globals(), globals())

def test_list_of_dicts():
    data = [
        {
            "test_int": 10,
            "test_str": "aaabbb"
        },

        {
            "test_int": 10
        }
    ]
    mapped_model = PythonDataModel(data)
    assert len(mapped_model.data) == 3

    generate_code = mapped_model.generate_code()
    exec(generate_code, globals(), globals())
