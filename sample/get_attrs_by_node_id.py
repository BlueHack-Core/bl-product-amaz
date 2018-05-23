from __future__ import print_function
from bl_product_amaz.us_btgs import US_btgs
from pprint import pprint

api_instance = US_btgs()

try:
    node_id = "2368343011"
    res = api_instance.get_attrs_by_node_id(node_id)
    pprint(res)

except Exception as e:
    print("Exception when calling get_attr_by_node_id: %s\n" % e)