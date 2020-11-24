from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from colorear import Model
import OpenSSL

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
color = Model()

@app.route('/<string:name>', methods=['GET'])
def Hellow(name):
    result = color.colorize(name)
    c = color.getComplement(result)
    response = {"color" : result, "complemento" : c}
    return response

if __name__ == "__main__":
    #app.run(host='10.158.0.4', port=4200, ssl_context='adhoc',debug=False)
    app.run(ssl_context='adhoc',debug=True)
