from __future__ import print_function
from bl_product_amaz.amz_attrs import AMZ_attrs
from pprint import pprint

api_instance = AMZ_attrs()

try:
    attr_id = "a0019"
    sub_attr_id = "aa0001000"
    res = api_instance.update_sub_attr_ids(attr_id, sub_attr_id)

    pprint(res)

except Exception as e:
    print("Exception when calling update_sub_attr_ids %s\n" % e)