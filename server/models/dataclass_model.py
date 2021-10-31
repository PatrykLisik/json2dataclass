from dataclasses import dataclass, field
from typing import List, Set, Dict, Union, Iterable

from server.models.json_to_dataclass_model import JsonModel


@dataclass
class PythonDataClassModelField:
    type_name: str
    filed_name: str


@dataclass
class PythonClassModel:
    name: str
    fields: List[PythonDataClassModelField] = field(default_factory=list)


@dataclass
class QueObject:
    type_name: str
    data: object


def is_primitive(value) -> bool:
    return isinstance(value, (int, str, float))


def generate_class_name(value, class_list) -> str:
    type_name = type(value).__name__
    if is_primitive(value):
        return type_name
    return f"{type_name}_{len(class_list)}"


class PythonDataModel:
    data: List[PythonClassModel]

    def __init__(self, data: Union[Dict, Set, List]):
        class_list: List[PythonClassModel] = []

        obj_to_analyze: List[QueObject] = [QueObject("JsonModel", data)]
        while len(obj_to_analyze) != 0:
            obj = obj_to_analyze.pop()
            obj_value = obj.data
            if isinstance(obj_value, dict):
                fields = []
                for key, value in obj_value.items():
                    type_name = generate_class_name(value, class_list)
                    # add to que is not primitive type
                    if is_primitive(value):
                        obj_to_analyze.append(QueObject(type_name=type_name, data=value))
                    obj_value = PythonDataClassModelField(filed_name=key, type_name=type_name)
                    fields.append(obj_value)
                class_list.append(PythonClassModel(name=obj.type_name, fields=fields))
            if isinstance(obj_value, Iterable):
                types_in_list = set()
                iterable_type = type(obj_value).__name__
                for value in obj_value:
                    type_name = generate_class_name(value, class_list)
                    types_in_list.add(type_name)
                    # add to que is not primitive type
                    if is_primitive(value):
                        obj_to_analyze.append(QueObject(type_name=type_name, data=value))

                if len(types_in_list) == 1:
                    # example List[int]
                    type_name = f"{iterable_type}[{types_in_list.pop()}]]"
                else:
                    # example List[Union[int,str]]
                    type_name = f"{iterable_type}[Union[{','.join(types_in_list)}]]"
                class_list.append(
                    PythonClassModel(name=obj.type_name, fields=[
                        PythonDataClassModelField(type_name=type_name, filed_name="items")]
                                     )
                )

        self.data = class_list[::-1]
