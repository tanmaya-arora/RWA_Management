import requests
import json 
from paytmchecksum import PaytmChecksum
import datetime
from django.views.decorators.csrf import csrf_exempt


PAYTM_MID = "XTuSTF64649388339128"
PAYTM_MERCHANT_KEY = "V8%MqlQ@MX8@WVhc"

PAYTM_ENVIRONMENT= 'https://securegw-stage.paytm.in'
PAYTM_WEBSITE= 'WEBSTAGING'

amount= '1.00'
order_id='order_'+str(datetime.datetime.now().timestamp())

@csrf_exempt
def getTransactionToken(request):
    try:
        paytmParams = dict()

        paytmParams["body"] = {
            "requestType": "Payment",
            "mid": PAYTM_MID,
            "websiteName": PAYTM_WEBSITE,
            "orderId": order_id,
            "callbackUrl": "http://127.0.0.1:5000/callback",
            "txnAmount": {
                "value": amount,
                "currency": "INR",
            },
            "userInfo": {
                "custId": "CUST_001",
            },
        }

        # Generate checksum by parameters we have in body
        checksum = PaytmChecksum.generateSignature(json.dumps(paytmParams["body"]), PAYTM_MERCHANT_KEY)

        paytmParams["head"] = {
            "signature": checksum
        }

        post_data = json.dumps(paytmParams)
        url = PAYTM_ENVIRONMENT + "/theia/api/v1/initiateTransaction?mid=" + PAYTM_MID + "&orderId=" + order_id
        response = requests.post(url, data=post_data, headers={"Content-type": "application/json"}).json()
        print(paytmParams)
        if response.get("body", {}).get("resultInfo", {}).get("resultStatus") == 'S':
            token = response.get("body", {}).get("txnToken", "")
        else:
            token = ""
        
        return token
    except Exception as e:
        # Handle exceptions here
        print("Error:", str(e))
        return ""
    

# def transactionStatus():
#   paytmParams = dict()
#   paytmParams["body"] = {
#     "mid" : PAYTM_MID,
#     # Enter your order id which needs to be check status for
#     "orderId" : "order_1647237662.654877",
#     }
  
#     checksum = PaytmChecksum.generateSignature(json.dumps(paytmParams["body"]), PAYTM_MERCHANT_KEY)

#     # head parameters
# paytmParams["head"] = {
#       "signature". : checksum
#     }

#     # prepare JSON string for request
#     post_data = json.dumps(paytmParams)

#     url = PAYTM_ENVIRONMENT+"/v3/order/status"

#     response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
#     response_str = json.dumps(response)
#     res = json.loads(response_str)
#     msg="Transaction Status Response"

#     return res['body']
