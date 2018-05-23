from __future__ import print_function
from bl_product_amaz.amz_attrs import AMZ_attrs
from pprint import pprint

api_instance = AMZ_attrs()

try:
    attr_id = "a0020"
    attr_kr_name = "테스트"
    attr_us_name = "test"
    res = api_instance.add_attr(attr_id, attr_kr_name, attr_us_name)

    pprint(res)

except Exception as e:
    print("Exception when calling add_attr %s\n" % e)