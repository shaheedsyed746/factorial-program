
from flask import Flask, render_template, request

app = Flask(__name__)

def factorial(n):
    if n < 0:
        raise ValueError("Negative numbers are not allowed")

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    number = ""

    if request.method == "POST":
        try:
            number = request.form["number"]
            n = int(number)

            if n < 0:
                result = "Enter a non-negative number"
            else:
                result = factorial(n)

        except ValueError:
            result = "Please enter a valid integer"

    return render_template(
        "index.html",
        result=result,
        number=number
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

