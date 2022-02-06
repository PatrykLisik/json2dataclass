# json2dataclass [![CircleCI](https://circleci.com/gh/PatrykLisik/json2dataclass/tree/master.svg?style=svg)](https://circleci.com/gh/PatrykLisik/json2dataclass/tree/master)

Heroku link: https://json2dataclass.herokuapp.com/
## Motivation
I have to do similar thing at work too many times. 
## How to run locally

`docker-compose up`

## What it does? 

Provides easy way to transform JSON to python dataclass structure.
Names of classes are probably going to need some change, but since every popular IDE provides rename functionally it should not be a problem.

![image](https://user-images.githubusercontent.com/14928623/152699167-7641339e-65da-4c01-9a70-829d6f576069.png)

## Encountered problems 

### Heterogeneous lists
Consider JSON that contains list with different types.
Even if variables' names are that same(`value_1`) program will generate two separate types.
```json
[
  {
    "value_1": "a"
  },
  {
    "value_1" : "b",
    "value_2" : "c"
  }
]
```
Code generated from JSON above.
```python
from typing import List, Set, Dict, Union, Iterable
from dataclasses import dataclass, field


@dataclass
class dict_0_0:
    value_1: str


@dataclass
class dict_0_1:
    value_1: str
    value_2: str


@dataclass
class JsonModel:
    items: list[Union[dict_0_0, dict_0_1]]
```