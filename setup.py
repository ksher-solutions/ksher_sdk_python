import codecs
import os
import sys


try:
    from setuptools import setup,find_packages
except:
    from distutils.core import setup,find_packages


with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
 

NAME = "ksher"
PACKAGES = ['hmac','hashlib','requests','urllib']
DESCRIPTION = "python implementation for Khser Payment API."
KEYWORDS = "Ksher, ksher, ksher-payment, ksher-payment-api, ksherpay"
AUTHOR = "Ksher"
AUTHOR_EMAIL = "support@ksher.com"
URL = "https://github.com/ksher-solutions/ksher_sdk_python"
VERSION = "0.1"
LICENSE = "MIT"

setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords = KEYWORDS,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    license = LICENSE,
    packages = find_packages(),
    install_requires=['requests >= 2.25.1'],
    include_package_data=True,
    zip_safe=True,
)
