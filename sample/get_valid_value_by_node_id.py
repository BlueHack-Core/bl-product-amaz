from __future__ import print_function
from pprint import pprint
from bl_product_amaz.us_btgs import US_btgs

api_instance = US_btgs()

try:

    res = api_instance.get_valid_value_by_node_id("13727922011")


    pprint(res)

except Exception as e:
    print("Exception when calling get_btg_by_node_id: %s\n" % e)
