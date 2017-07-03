__metaclass__ = type

from microsoftbotframework import MsBot
from tasks import *
import os

#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    if req.get("result").get("action") != "checkBitcoin":
        return {}
    baseurl = "https://api.korbit.co.kr/v1/ticker"
    result = urlopen(baseurl).read()
    data = json.loads(result)
    res = makeWebhookResult(data)
    return res

def makeWebhookResult(data):
    query = data.get('query')
    if query is None:
        return {}

    result = query.get('results')
    if result is None:
        return {}

    channel = result.get('channel')
    if channel is None:
        return {}

    price = channel.get('last')
    #location = channel.get('location')
    #units = channel.get('units')
    #if (location is None) or (item is None) or (units is None):
    #    return {}

    #price = item.get('condition')
    #if condition is None:
    #    return {}

    # print(json.dumps(item, indent=4))

    speech = "Today: " + price.get('last')

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
