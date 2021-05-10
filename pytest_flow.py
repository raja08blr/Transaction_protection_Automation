import pytest
from selenium import webdriver
import time
from common_functions_library import *
import subprocess
from datetime import datetime
from test_ecommerce_domain_tcpdump import *

@pytest.mark.ecommerce
def test_amazon_without_extension():
    amazon(0)


@pytest.mark.ecommerce
def test_amazon_with_extension():
    amazon(1)


@pytest.mark.sports
def test_less():
    num = 100
    assert num < 200
