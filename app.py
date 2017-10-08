import os
import requests
import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)
base_url = 'https://ifsc.razorpay.com/'

@ask.launch
def new_request():
    return question("What do you want me to do?")

@ask.intent("FetchIFSCdetails")
def fetch_IFSC_details():
    return question('What is IFSC code?').reprompt('May I please have the IFSC code?')

@ask.intent("IFSCCode")
def ifsc_details(bankA, bankB, bankC, bankD, bankE, bankF, bankG, bankH, bankI, bankJ, bankK):
    ifsc = bankA + bankB + bankC + bankD + bankE + bankF + bankG + bankH + bankI + bankJ + bankK
    url = base_url + ifsc
    r = requests.get(url)
    json_data = r.json()
    return statement('The details are' + ' ' + json_data['BANK'] + ' ' + json_data['BRANCH'] + ' ' + json_data['ADDRESS'])


port = int(os.getenv('PORT', 5000))
app.run(debug=False, port=port, host='0.0.0.0')
