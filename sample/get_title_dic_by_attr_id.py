from __future__ import print_function
from bl_product_amaz.amz_attrs import AMZ_attrs
from pprint import pprint

api_instance = AMZ_attrs()

try:
    attr_id = "a0001"
    res = api_instance.get_title_dic_by_attr_id(attr_id)

    pprint(res)

except Exception as e:
    print("Exception when calling get_title_dic_by_attr_id %s\n" % e)