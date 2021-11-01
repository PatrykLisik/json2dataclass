from sanic import Sanic
from sanic.response import text, json

from models.dataclass_model import PythonDataModel

app = Sanic("Json2Dataclass")


@app.post("/api/to_dataclass")
async def to_dataclass(request):
    to_parse = request.json["json_to_convert"]
    mapped_model = PythonDataModel(to_parse).generate_code()
    return json({
        "dataclass": mapped_model
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, auto_reload=True)
