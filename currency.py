from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route("/")
def main():

    return render_template("start.html")

@app.route("/convert")
def convert():

    amount = request.args.get('amount')
    base = request.args.get('from').upper()
    other = request.args.get('to').upper()

    if base is None or other is None:	
        return render_template("start.html")

    if amount is "":
        amount = "1"

    res = requests.get("https://api.exchangeratesapi.io/latest",
                        params={"base": base, "symbols": other})

    if res.status_code != 200:
        return render_template("error.html")

    data = res.json()
    rate = data["rates"][other]
    ans = float(amount)*float(rate)

    return render_template("answer.html", ans = ans, amount = amount, base = base, rate = rate, other = other)

if __name__ == '__main__':
    app.run(debug=True)


