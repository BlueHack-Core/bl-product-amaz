from __future__ import print_function
from bl_product_amaz.amz_sub_attrs import AMZ_sub_attrs
from pprint import pprint

api_instance = AMZ_sub_attrs()

try:
    sub_attr_id = "aa0000001"
    res = api_instance.get_sub_attr_by_sub_attr_id(sub_attr_id)
    pprint(res)

except Exception as e:
    print("Exception when calling get_sub_attr_by_sub_attr_id: %s\n" % e)