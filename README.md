# ksher_sdk_python
Ksher python Library at http://api.ksher.net

## How to install

```console
pip3 install ksher
```

```
from ksher.ksher_pay_sdk import KsherPay

appid=mch35005
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
data['mch_order_no'] = generate_order_id()
resp = payment_handle.gateway_pay(data)


```