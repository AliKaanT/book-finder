from flask import Flask, render_template, request
from core import core

app = Flask(__name__)


@app.route("/")
def test():
    return render_template("index.html", content="Hello, World!")


@app.route("/post", methods=["POST"])
def hello_world():
    user_input = request.form.get("message")
    llm_output = core(user_input)
    print(llm_output)
    return render_template(
        "index.html",
        name=llm_output.get("name"),
        author=llm_output.get("author"),
        turkish_name=llm_output.get("turkish_name"),
        price=llm_output.get("price"),
        url=llm_output.get("url"),
    )


app.run()
