from __future__ import print_function
from bl_product_amaz.amz_sub_attrs import AMZ_sub_attrs
from pprint import pprint

api_instance = AMZ_sub_attrs()


try:
    sub_attr_id = "aa1000000"
    sub_attr_kr_name = "테스트"
    sub_attr_us_name = "test"
    res = api_instance.add_sub_attr(sub_attr_id, sub_attr_kr_name, sub_attr_us_name)

except Exception as e:
    print("Exception when calling add_sub_attr: %s\n" % e)