from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('aaronroach_cv.html')

if __name__ == '__main__':
   app.run()