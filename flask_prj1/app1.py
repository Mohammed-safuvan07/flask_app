from flask import Flask,request


app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Data Science Internship Page'

@app.route('/about')
def about():
    return 'The Innomatics Research Labs providing an Data Science Online Internship  '

@app.route('/user')
def names():
    name1 = request.args.get('name1')
    name2 = request.args.get('name2')
    return (name1.upper()+" "+name2.upper())

@app.route('/addition')
def operations():
    a = request.args.get('a')    
    b = request.args.get('b')
    return str(int(a)+int(b))
    
@app.route('/sub')
def sub():
    a = request.args.get('a')    
    b = request.args.get('b')
    return str(int(a)-int(b))        
      
         

        
        


if __name__ == '__main__':
    app.run(debug=True)