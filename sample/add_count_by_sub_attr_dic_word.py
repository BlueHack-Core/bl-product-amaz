from __future__ import print_function
from bl_product_amaz.amz_title_dic import AMZ_title_dic
from pprint import pprint


api_instance = AMZ_title_dic()

try:
    sub_attr_id = "3/4 sleeve"
    res = api_instance.add_count_by_sub_attr_dic_word(sub_attr_id, count_up_num=3)
    pprint(res)

except Exception as e:
    print("Exception when calling add_count_by_sub_attr_code: %s\n" % e)