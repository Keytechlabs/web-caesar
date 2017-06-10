from flask import Flask, request  
app = Flask(__name__)
app.config['DEBUG'] =True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
       <form method="post">
          <label for= "rot"> Rotate by: </label>
          <input id="text" type="text" name="rot" value ="0" />
             <textarea ="text"> </textarea>
          <input type="submit"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST']) 
def encrypt():
    rot  = request.form['rot']
    text = request.form['text']
    encrypted_text = rotate_string.encrypt(text)
    return '<h1/>' + encrypted_text + '</h1>'
    
app.run()