
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <h3>Calculator</h3>
    <form action="/calc">
        <input name="a" placeholder="First number" required>
        <select name="op">
            <option value="add">Add</option>
            <option value="sub">Subtract</option>
        </select>
        <input name="b" placeholder="Second number" required>
        <button>Calculate</button>
    </form>
    '''

@app.route("/calc")
def calc():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    op = request.args.get("op")

    if op == "add":
        r = a + b
    else:
        r = a - b

    return f"Result: {r}"

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
