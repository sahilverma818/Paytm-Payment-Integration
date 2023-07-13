from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import PaytmChecksum

MERCHANT_KEY = 'YOUR_MERCHANT_KEY'
# Create your views here.
def payment(request):
    # Request Company to transfer the amount
    param_dict={

            'MID': 'YOUR_MERCHANT_ID',
            'ORDER_ID': 'dddgfgfeeed',
            'TXN_AMOUNT': '1',
            'CUST_ID': 'XYZ@GMAIL.COM',
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/',

    }
    param_dict['CHECKSUMHASH'] = PaytmChecksum.generateSignature(param_dict, MERCHANT_KEY)
    return  render(request, 'paytm.html', {'param_dict': param_dict})

@csrf_exempt
def handlerequest(request):
    # Company will send you post request here
    form = request.POST
    responce_dict = {}
    for i in form.keys():
        responce_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = PaytmChecksum.verifySignature(responce_dict, MERCHANT_KEY, checksum)
    if verify:
        if responce_dict['RESPONSE'] == '01':
            print("Order Successful")
        else:
            print("Order Not Successful because", responce_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response' : responce_dict})