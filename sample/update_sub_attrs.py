from __future__ import print_function
from bl_product_amaz.amz_attrs import AMZ_attrs
from pprint import pprint

api_instance = AMZ_attrs()

try:

    res = api_instance.update_sub_attrs("1004", "2034")
    pprint(res)

except Exception as e:
    print("Exception when calling update_sub_attrs: %s\n" % e)