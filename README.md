# Ksher SDK for Python

[![Python Package](https://github.com/ksher-solutions/ksher_sdk_python/actions/workflows/python-publish.yml/badge.svg)](https://github.com/ksher-solutions/ksher_sdk_python/actions/workflows/python-publish.yml)
[![Version](https://img.shields.io/pypi/v/ksher)](https://pypi.org/project/ksher/)

Ksher payment SDK for Python.

📄 **Documentation**: [API Reference](http://api.ksher.net)

## Available SDKs
Ksher SDK is available in multiple languages:
- **Java**: [Ksher SDK (Java)](https://github.com/ksher-api/ksher-sdk/tree/master/java)
- **Python**: [Ksher SDK (Python)](https://github.com/ksher-solutions/ksher_sdk_python)
- **Go**: [Ksher SDK (Go)](https://github.com/ksher-api/ksher-sdk/tree/master/go)
- **PHP**: [Ksher SDK (PHP)](https://github.com/ksher-api/ksher-sdk/tree/master/php)
- **.NET Core**: [Ksher SDK (.NET Core)](https://github.com/ksher-api/ksher-sdk/tree/master/netcore)
- **Node.js**: [Ksher SDK (Node.js)](https://github.com/ksher-solutions/ksher_sdk_nodejs)

---

## 📦 Installation

There are two ways to install this package:

### Option 1: Install via Pip
```sh
pip install ksher
```

### Option 2: Clone and Install Manually
#### Step 1: Clone the Repository
```sh
git clone https://github.com/ksher-solutions/ksher_sdk_python.git
```

#### Step 2: Navigate and Install Dependencies
```sh
cd ksher_sdk_python
pip install -r requirements.txt
pip install .
```

Alternatively, install locally with:
```sh
pip install ./ksher_sdk_python --user
```

---

## 🚀 How to Use
First, initialize the payment object to perform various payment actions:
- **Initialize Payment Object**
- **Create New Order**
- **Query Order Status**
- **Refund an Order**

### 🔹 Redirect API (Default)
To use the **Redirect API**, initialize as follows:
```python
from ksher.ksher_pay_sdk import KsherPay

appid = "mch35000"
privatekey = "/path/to/mch_privkey.pem"
pubkey = "/path/to/ksher_pubkey.pem"

payment_handle = KsherPay(appid, privatekey, pubkey)
data = {
    "total_fee": "100",
    "fee_type": "THB",
    "mch_code": "",
    "refer_url": "http://www.example.com",
    "mch_redirect_url": "http://www.example.com/success",
    "mch_redirect_url_fail": "http://www.example.com/fail",
    "mch_notify_url": "http://www.example.com/notify",
    "product_name": "",
    "channel_list": "promptpay,linepay,airpay,truemoney,atome,card,ktc_instal,kbank_instal,kcc_instal,kfc_instal,scb_easy,bbl_deeplink,baybank_deeplink,kplus,alipay,wechat,card,ktc_instal,kbank_instal,kcc_instal,kfc_instal"
}
data['mch_order_no'] = "HelloWebsite"
resp = payment_handle.gateway_pay(data)
```

### 🔹 C_Scan_B API (QR Code Payment)
To use the **C_Scan_B API**, specify the API type when initializing:
```python
from ksher.ksher_pay_sdk import KsherPay

appid = "mch35000"
privatekey = "/path/to/mch_privkey.pem"
pubkey = "/path/to/ksher_pubkey.pem"

payment_handle = KsherPay(appid, privatekey, pubkey)
data = {
    "mch_order_no": "202208101150",
    "total_fee": "100",
    "fee_type": "THB",
    "channel": "promptpay",
    "notify_url": "http://www.example.com/notify"
}
data['mch_order_no'] = "HelloKiosk"
resp = payment_handle.native_pay(data)
```

---

## 📌 Notes
- Ensure that the `appid`, `privatekey`, and `pubkey` are correctly set.
- Replace URLs with your actual endpoint URLs.
- `pubkey` inside SDK, The file name is `ksher_pubkey.pem`. This value is optional, you not need to pass with it.
- Use the correct `channel_list` based on your integration.

---

📖 For full documentation, visit [Ksher API Docs](http://api.ksher.net).

