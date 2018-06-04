from __future__ import print_function
from bl_product_amaz.amz_title_dic import AMZ_title_dic
from pprint import pprint

api_instance = AMZ_title_dic()

try:
    sub_attr_id = "aa0000003"
    res = api_instance.reset_count_to_zero_by_sub_attr_id(sub_attr_id)
    pprint(res)

except Exception as e:
    print("Exception when calling add_count_by_sub_attr_code: %s\n" % e)