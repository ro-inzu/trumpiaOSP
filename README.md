# trumpiaOSP
A simple online signup page that uses the Trumpia API resources for adding new contacts

![PyPI - Python Version](https://img.shields.io/badge/python-3.7-blue)
![PyPI - Flask Version](https://img.shields.io/badge/flask-1.1-orange)
![PyPI - Requests Version](https://img.shields.io/badge/requests-2.22-green)

![Screenshot](/screenshot/preview.png)
![Screenshot](/screenshot/incorrectdata.png)
![Screenshot](/screenshot/response.png)
![Screenshot](/screenshot/missingNumber.png)
![Screenshot](/screenshot/success.png)
![Screenshot](/screenshot/invalid.png)
![Screenshot](/screenshot/checkBox.png)
![Screenshot](/screenshot/liveAWS.png)
![Screenshot](/screenshot/awsEBconfig.png)

Trumpia API class for subscriptions
- PUT SUBSCRIPTION
- GET REPORT FOR PUT SUBSCRIPTION
- POST SUBSCRIPTION
- GET REPORT FOR POST SUBSCRIPTION
- GET SEARCH SUBSCRIPTION by mobile number
- GET SUBSCRIPTION BY SPECIFIC ID

### Setup
- (Recommended) create your virtual environment
  - python3.7 -m venv env
    - source env/bin/activate
- install requests
  - python3.7 -m pip install requests, flask

### Flow
- app.py has two functions
    - trmOSP(): calls subscriptions after getting POST information from the form
    - subscription(): adds new contacts/updates existing contacts (first and or last name only)

## API Documentation
 - [Trumpia REST API](http://classic.trumpia.com/api/docs/rest/overview.php)
 - [Trumpia Subscriptions](http://classic.trumpia.com/api/docs/rest/functions/subscription.php)
 - [Trumpia Lists](http://classic.trumpia.com/api/docs/rest/functions/list.php)
 - [Trumpia SMS Direct](http://classic.trumpia.com/api/docs/rest/functions/direct-sms.php)
 - [Trumpia Status Report](http://classic.trumpia.com/api/docs/rest/functions/report.php)
 - [Trumpia System Status Codes](http://classic.trumpia.com/api/docs/rest/status-code.php)

## Deploying a Flask APP on AWS Beanstalk
- [AWS Beanstalk](https://towardsdatascience.com/deploying-a-flask-application-on-aws-elastic-beanstalk-via-cli-c0e93548472e)
- [WSGI PATH](https://stackoverflow.com/questions/31169260/your-wsgipath-refers-to-a-file-that-does-not-exist)
- WSGI path error use command "eb config": Under WSGI path refer to my screenshot. Should be the name of your app. 
