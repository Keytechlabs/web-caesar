from flask import Flask, request  
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] =True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                <!--reading background color wrong,why?-->
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
       <form action="" method="post">
          <label for= "rot"> Rotate by: </label>
          <input id="text" type="text" name="rot" value ="0" />
             <textarea name ="text"> {0} </textarea>
          <input type="submit" value="submit"/>
          <!---Error code line 33 raise value?-->
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=["POST"])
def encrypt():
    encryptRot =  request.form['rot']
    encryptText = request.form['text']

    encryptRot = int(encryptRot)

    encrypted = rotate_string(encryptText, encryptRot)
    return form.format(encrypted)
    
app.run()