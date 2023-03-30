# ksher sdk python

[![Python Package](https://github.com/ksher-solutions/ksher_sdk_python/actions/workflows/python-publish.yml/badge.svg)](https://github.com/ksher-solutions/ksher_sdk_python/actions/workflows/python-publish.yml)
[![Version](https://img.shields.io/pypi/v/ksher)](https://pypi.org/project/ksher/)

Ksher payment SDK for Python. Please check document at http://api.ksher.net

Another SDK please check at

Java: https://github.com/ksher-api/ksher-sdk/tree/master/java

Python: https://github.com/ksher-solutions/ksher_sdk_python

Go: https://github.com/ksher-api/ksher-sdk/tree/master/go

PHP: https://github.com/ksher-api/ksher-sdk/tree/master/php

Netcore: https://github.com/ksher-api/ksher-sdk/tree/master/netcore

NodeJs: https://github.com/ksher-solutions/ksher_sdk_nodejs

## How to Install

there are two option two install this package;

1. Pip Install This package
2. Clone this repository

### Option 1: Pip Install This package
```
pip install ksherpay
```

### Option 2: Clone this repository

#### Step1: clone this repository
```shell
git clone https://github.com/ksher-solutions/ksher_sdk_python.git
```

#### Step2: cd into cloned source code and pip install all the requriements and the package itself
```shell
cd ksher_sdk_python
pip install -r requirements.txt
pip install .

```

or if you want to pip install from local please use
```
pip install ./ksher_sdk_python --user 
```

## How to Use
you need to first init the payment object and that you can use it to;
- Init Payment Object
- Create New Order
- Query Order Status
- Refund the Order

#### Redirect API

the default api is redirect api you can just init it like this


```python
from ksher.ksher_pay_sdk import KsherPay

appid=mch35000
privatekey=/Users/yourpath/repo/ksher_sdk_python/mch_privkey.pem
pubkey=/Users/yourpath/repo/ksher_sdk_python/ksher_pubkey.pem

payment_handle = KsherPay(appid, privatekey, pubkey)
data = {
    "total_fee": "100",
    "fee_type": "THB",
    "mch_code": "",
    "refer_url": "http://www.baidu.com",
    "mch_redirect_url":"http://www.baidu.com/api/gateway_pay/success",
    "mch_redirect_url_fail":"http://www.baidu.com/api/gateway_pay/fail",
    "mch_notify_url":"http://www.baidu.com/api/gateway_pay/notify_url/",
    "product_name":"",
    "channel_list":"promptpay,linepay,airpay,truemoney,atome,card,ktc_instal,kbank_instal,kcc_instal,kfc_instal,scb_easy,bbl_deeplink,baybank_deeplink,kplus,alipay,wechat,card,ktc_instal,kbank_instal,kcc_instal,kfc_instal"
}
data['mch_order_no'] = "HelloWebsite"
resp = payment_handle.gateway_pay(data)
```

#### C_Scan_B API
to use 'C_Scan_B API', you need to specified it when init the object

**as shown in the code, please use ksher package's provided value to specified the appid/privatekey value**

```python
from ksher.ksher_pay_sdk import KsherPay

appid=mch35000
privatekey=/Users/yourpath/repo/ksher_sdk_python/mch_privkey.pem
pubkey=/Users/yourpath/repo/ksher_sdk_python/ksher_pubkey.pem

payment_handle = KsherPay(appid, privatekey, pubkey)
data = {
    "mch_order_no": "202208101150",
    "total_fee": "100",
    "fee_type":"THB",
    "channel": "promptpay",
    "notify_url": "http://www.baidu.com/api/gateway_pay/notify_url/"
}
data['mch_order_no'] = "HelloKiosk"
resp = payment_handle.native_pay(data)
```
