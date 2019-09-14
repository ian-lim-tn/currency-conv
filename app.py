from flask import Flask, escape, request, render_template
import json
import requests

app = Flask(__name__)

if __name__ == '__main__':
   app.run(debug = True)
   app.run()

@app.route('/')

def index():
   return render_template("index.html")

@app.route('/convert', methods=['GET', 'POST'])

def form():
   while request.method == 'POST':
      try:
         amount = float(request.form['amount'])
      except:
         conversion = "Please enter a number to proceed"
         return render_template("index.html", conversion=conversion)
         

      amount = float(request.form['amount'])
      btn_val = request.form['btn-val']
      print(type(amount))
      print(btn_val)

      symbols_val = f"MYR,{btn_val}"

      print(symbols_val)

      # # To get data from finance API
      api_call = requests.get('http://data.fixer.io/api/latest?access_key=64462d177fc6f5eddae277f0290382a3&symbols='+ symbols_val)

      print(api_call)

      # # # To get the rates for each currencies using European Euro (EUR) as the base currency
      data = api_call.json()

      print(data)

      try:
         btn_val = data['rates'][btn_val]
         # JPY = data['rates']['JPY']
         # SGD = data['rates']['SGD']
         MYR = data['rates']['MYR']
         # EUR = data['rates']['EUR']
      except:
        print("\nPlease input only numeric!\n")



      # # From the conversion of EUR to MYR with MYR as base currency
      msiaRinggit = amount / MYR

      print(msiaRinggit)

      # # Conversion formulas from MYR to other currencies
      conversion = round(msiaRinggit * btn_val,2)

      # print(conversion)
      # # conversionJPY = msiaRinggit * JPY
      # # conversionSGD = msiaRinggit * SGD

      print(conversion)



      # return conversion
      return render_template("index.html", conversion=conversion)
      # return str(conversion)








