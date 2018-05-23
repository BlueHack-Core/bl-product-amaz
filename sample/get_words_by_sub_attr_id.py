from __future__ import print_function
from bl_product_amaz.amz_title_dic import AMZ_title_dic
from pprint import pprint

api_instance = AMZ_title_dic()

try:
    offset=0
    limit=50
    sub_attr_id = "aa0000003"
    while True:
        res = api_instance.get_words_by_sub_attr_id(sub_attr_id, offset, limit)

        if limit > len(res):
            break
        else:
            offset = offset + limit

    pprint(res)

except Exception as e:
    print("Exception when calling get_words_bt_sub_attr_id %s\n" % e)