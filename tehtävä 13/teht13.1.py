from flask import Flask
app = Flask(__name__)


@app.route('/alkuluku/<number>')
def alkuluku(number):
    number = float(number)
    isprime = calculator(number)

    result = {
        "Number": number,
        "isPrime": isprime
    }
    return result


def calculator(outcome):
    if outcome > 1:
        for m in range(2, int(outcome / 2) + 1):
            if (outcome % m) == 0:
                return "false"
        else:
            return "true"
    else:
        return "false"


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)