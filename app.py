from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to flask'

@app.route('/cal',methods=['GET','POST'])
def math_operator():
    operatation=request.json['operation']
    number1=request.json['number1']
    number2=request.json['number2']
    
    if operatation=='add':
        result=number1+number2
    elif operatation=='sub':
        result=number1-number2
    elif operatation=='mul':
        result=number1*number2
    elif operatation=='div':
        result=number1/number2
    else:
        return jsonify('Invalid operartion type, it should be in (add,sub,mul,div)')

    return jsonify(f'result is: {result}')


if __name__=='__main__':
    app.run(port=8080,debug=True)
