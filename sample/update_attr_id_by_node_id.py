from __future__ import print_function
from bl_product_amaz.us_btgs import US_btgs
from pprint import pprint

api_instance = US_btgs()

try:
    node_id = "5418126011"
    attr_id = "a0001"
    res = api_instance.update_attr_id_by_node_id(node_id,attr_id)
    pprint(res)

except Exception as e:
    print("Exception when calling update_attr_id_by_node_id: %s\n" % e)