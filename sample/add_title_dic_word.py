from __future__ import print_function
from bl_product_amaz.amz_title_dic import AMZ_title_dic
from pprint import pprint

api_instance = AMZ_title_dic()

try:
    sub_attr_id = "aa0000000"
    sub_attr_dic_word = "test"
    res = api_instance.add_title_dic_word(sub_attr_id, sub_attr_dic_word)


    pprint(res)

except Exception as e:
    print("Exception when calling add_title_dic_word %s\n" % e)