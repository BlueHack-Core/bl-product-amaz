from __future__ import print_function
from bl_product_amaz.amz_attrs import AMZ_attrs
from pprint import pprint

api_instance = AMZ_attrs()

try:
    res = api_instance.get_sub_attr_by_attr_id("a0001")

    pprint(res)

except Exception as e:
    print("Exception when calling get_sub_attr_by_attr_id %s\n" % e)