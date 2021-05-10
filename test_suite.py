from ecommerce_domain import *
from common_functions_library import *
import pytest

data = read_config_file('/root/dynamic_analysis_framework/config_ext_ids.txt')
download_crx(data['ext_id'])
run_tcpdump_on_local_machine(0,amazon())
run_tcpdump_on_local_machine(1,amazon())


# @pytest.mark.ecommerce
# @pytest.mark.socialNetwork
# def test_download_extension_crx_file():
#     data = read_config_file('/root/dynamic_analysis_framework/config_ext_ids.txt')
#     download_crx(data['ext_id'])
