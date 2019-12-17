#app.py
from driver import subscriptions, isValid
from flask import Flask, request, render_template #import main Flask class and request trm_object
import time

app = Flask(__name__) #create the Flask app


@app.route('/', methods = ['GET','POST'])
def trmOSP():
    if request.method == 'POST': #this block is only entered when the form is submitted
        first_name = request.form.get('firstname')
        last_name = request.form['lastname']
        mobile_number = request.form['mobile_number']
        #checks if the mobile number is valid
        if(isValid(mobile_number)):
             subscriptions(mobile_number,first_name,last_name)
             results = "valid"
             return render_template('index.html',results = results)
        else:
            print('not valid')
            results = "invalid"
            return render_template('index.html',results = results)

    return render_template('index.html')

if __name__ == '__main_':
    app.run(debug=True, host="0.0.0.0") #run app in debug mode on port 5000
