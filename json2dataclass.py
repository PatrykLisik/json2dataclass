from flask import Flask, request, render_template, abort

from .models.dataclass_model import PythonDataModel

app = Flask(__name__,static_folder="")


@app.post("/api/to_dataclass")
def to_dataclass():
    try:
        to_parse = request.json["json_to_convert"]
        mapped_model = PythonDataModel(to_parse).generate_code()
        return {
            "dataclass": mapped_model
        }
    except Exception as e:
        app.logger.error(f"Request payload {request.json}")
        app.logger.error(e)
        abort(500, "Internal Error")


@app.get("/")
def index():
    return render_template('index.html')
