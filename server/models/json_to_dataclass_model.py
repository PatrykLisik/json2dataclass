from dataclasses import dataclass, field
from numbers import Number
from typing import List, Dict, Union


@dataclass
class JsonDictModelField:
    pass


@dataclass
class JsonDictModel:
    fields: List[JsonDictModelField] = field(default_factory=list)

    def __init__(self, json_object: dict):
        fields = []
        for key, value in json_object.items():
            fields.append(JsonDictModelField(key=key, value=value))
        self.fields = fields


@dataclass
class JsonDictModelField:
    key: str = field(hash=True)
    value: Union[str, Number, List, JsonDictModel]

    def __init__(self, key, value):
        self.key = key
        if isinstance(value, dict):
            self.value = JsonDictModel(value)
        else:
            self.value = value
