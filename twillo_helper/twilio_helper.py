### Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from pathlib import Path

### Set environment variables in AWS SageMaker Notebook Instance Lifecircle Configuration.
### https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html
### Bash script example refers to lifecircle_configuration_script_example.sh in this folder.
### Windows user be aware of replacing line ending CRLF ('\r\n') with LF ('\n').

### Your Account Sid and Auth Token from twilio.com/console
### and set the environment variables. See http://twil.io/secure
import os
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
number_from = os.environ['TWILIO_NUMBER_FROM']
number_to = os.environ['TWILIO_NUMBER_TO']
client = Client(account_sid, auth_token)

### If you are using json file to store the secrets:
# import json
# filename = str(Path(__file__).parent.absolute()) + '/twilio.json'
# with open(filename) as f:
#     twilio_config = json.load(f)
# client = Client(twilio_config['account_sid'], twilio_config['auth_token'])
# number_from = twilio_config['number_from']
# number_to = twilio_config['number_to']

def send_text_message(body='Text message from Twilio',
                    #   media_url=['https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg']
                      from_=number_from,
                      to=number_to
                     ):
    message = client.messages \
        .create(
            body=body,
            # media_url=media_url,
            from_=from_,
            to=to
        )
    print('Text message sent:', message.sid)