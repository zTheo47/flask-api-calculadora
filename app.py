from flask import Flask, request, jsonify
import ast
import operator

app = Flask(__name__)

ops = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow
}

def eval_expr(node):
    if isinstance(node, ast.BinOp):
        return ops[type(node.op)](
            eval_expr(node.left),
            eval_expr(node.right)
        )
    elif isinstance(node, ast.Constant):
        return node.value
    else:
        raise ValueError("Expressão inválida")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    expr = data["expression"]

    expr = expr.replace("x", str(data.get("x", 0)))
    tree = ast.parse(expr, mode="eval")
    result = eval_expr(tree.body)

    return jsonify({"result": result})

@app.route("/ping", methods=["GET"])
def ping():
    return {"message": "API online"}

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)