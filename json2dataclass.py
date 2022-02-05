from flask import Flask, request

from .models.dataclass_model import PythonDataModel

app = Flask(__name__)


@app.post("/api/to_dataclass")
def to_dataclass():
    to_parse = request.json["json_to_convert"]
    mapped_model = PythonDataModel(to_parse).generate_code()
    return {
        "dataclass": mapped_model
    }


@app.get("/")
def index():
    return "hello"
