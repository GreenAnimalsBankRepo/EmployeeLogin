from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import hashlib
import base64
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import urllib.parse

LOGIN_PAGE = {
    'customer_id': '400235',
    'merchant_id': '496',
    'username': 'admin',
    'password': 'gbank123',
    'login_url': 'https://employee.greenanimalsbank.com',
} # DEBUG == True şeklinde kontrol yaparak prod'a göre conf yapabilirsiniz


def index(request):
    return render(request, 'index.html')


@require_http_methods(['POST'])




@require_http_methods(['POST'])
@csrf_exempt
def ok_url(request):
    gelen = request.POST.get('AuthenticationResponse')
    data = urllib.parse.unquote(gelen)
    merchant_order_id_start = data.find('<MerchantOrderId>')
    merchant_order_id_stop = data.find('</MerchantOrderId>')
    merchant_order_id = data[merchant_order_id_start + 17:merchant_order_id_stop]
    amount_start = data.find('<Amount>')
    amount_end = data.find('</Amount>')
    amount = data[amount_start + 8:amount_end]
    md_start = data.find('<MD>')
    md_end = data.find('</MD>')
    md = data[md_start + 4:md_end]
    hashed_password = base64.b64encode(
        hashlib.sha1(LOGIN_PAGE["password"].encode('ISO-8859-9')).digest()).decode()
    hashed_data = base64.b64encode(hashlib.sha1(
        f'{LOGIN_PAGE["merchant_id"]}{merchant_order_id}{amount}{SANAL_POS["username"]}{hashed_password}'.encode(
            "ISO-8859-9")).digest()).decode()
    xml = f"""

    headers = {'Content-Type': 'application/xml'}
    r = requests.post(SANAL_POS['odeme_onay_url'], data=xml.encode('ISO-8859-9'), headers=headers)
    return HttpResponse(r)


@require_http_methods(['POST'])
@csrf_exempt
def fail_url(request):
    pass
