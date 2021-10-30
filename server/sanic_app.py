from sanic import Sanic
from sanic.response import text

app = Sanic("Json2Dataclass")


@app.post("/")
async def hello_world(request):
    return text("Hello, world")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, auto_reload=True)
