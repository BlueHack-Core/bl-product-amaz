from __future__ import print_function
from bl_product_amaz.amz_sub_attrs import AMZ_sub_attrs
from pprint import pprint

api_instance = AMZ_sub_attrs()

try:
    res = api_instance.add_count_by_sub_attr_code("2001")
    pprint(res)

except Exception as e:
    print("Exception when calling add_count_by_sub_attr_code: %s\n" % e)