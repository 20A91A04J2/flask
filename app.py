
from flask import Flask
app = Flask(__name__)
  
@app.route('/')
def hello():
    return "Rising phoenix did it"
  
  
if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = True) 
