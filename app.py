from flask import Flask, redirect, render_template, request,url_for, flash, session
import base64
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from io import BytesIO
import cv2
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a secret key here'



@app.route("/", methods = ['GET', 'POST'])
def home():
     status = str(session.get("status"))
     # status = str(request.args.get("status"))
     print(status)
     return render_template('home.html',topic=status)



@app.route("/img", methods=['GET', 'POST'])
def img():  
     if request.method == "POST":
          l1= []
          model = keras.models.load_model("mnist_model.keras")
          newx = request.form.get('data')
          content = newx.split(';')[1]
          newy = content.split(',')[1]
          body = base64.decodebytes(newy.encode('utf-8'))
          im = Image.open(BytesIO(body))
          image = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
          grey = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
          ret, thresh = cv2.threshold(grey.copy(), 75, 255, cv2.THRESH_BINARY_INV)
          contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
          preprocessed_digits = []
          for c in contours:
               x,y,w,h = cv2.boundingRect(c)
               cv2.rectangle(image, (x,y), (x+w, y+h), color=(0, 255, 0), thickness=2)
               digit = thresh[y:y+h, x:x+w]
               resized_digit = cv2.resize(digit, (18,18)) 
               padded_digit = np.pad(resized_digit, ((5,5),(5,5)), "constant", constant_values=0)
               preprocessed_digits.append(padded_digit)
          inp = np.array(preprocessed_digits)
          for digit in preprocessed_digits:
               prediction = model.predict(digit.reshape(1, 28*28))   
               l1.append(np.argmax(prediction))
          print(l1)
          l1= l1[::-1]
          " ".join(str(l1))
          y_pred = " ".join(str(l1))
          session["status"] = str(y_pred)
          return redirect(url_for('home',status=y_pred))  
     if request.method=="GET":
            return "dont access this page directly"    


if __name__ == "__main__":
     app.run(debug=True)