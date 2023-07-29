from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to flask'

@app.route('/cal',methods=['GET'])
def math_operator():
    return ''


if __name__=='__main__':
    app.run(port=8080,debug=True)
