from flask import Flask, request, jsonify, render_template
from lexer import Lexer
from parser import Parser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/analyze', methods=['POST'])
def analyze():
    curp = request.form.get('curp', '')

    lexer = Lexer(curp)
    lexer.tokenize()  
    tokens = lexer.get_tokens()  

    parser = Parser(lexer)
    parser.parse()  
    syntactic_validation = parser.get_validation_message()

    response = {
        "lexical_analysis": tokens if tokens else None,
        "syntactic_validation": syntactic_validation
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
