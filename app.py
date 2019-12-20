#app.py
from subscripts import subscriptionHandler as subcription
from subscripts import validateFormat as validate
from flask import Flask, request, render_template #import main Flask class and request trm_object
import time

application = Flask(__name__) #create the Flask app
app = application

@app.route('/', methods = ['GET','POST'])
def trmOSP():
    if request.method == 'POST': #this block is only entered when the form is submitted
        first_name = request.form.get('firstname')
        last_name = request.form['lastname']
        mobile_number = request.form['mobile_number']
        #checks if the mobile number is valid
        if(validate.isValid(mobile_number)):
            results = subcription.subscriptions(mobile_number,first_name,last_name)
            if results == None:
                 results = "valid"
            return render_template('index.html',results = results)
        else:
            results = "invalid"
            return render_template('index.html',results = results)

    return render_template('index.html',results = "none")

if __name__ == '__main_':
    app.run(debug=True)
