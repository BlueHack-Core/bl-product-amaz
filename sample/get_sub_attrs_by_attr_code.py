from __future__ import print_function
from bl_product_amaz.amz_attrs import AMZ_attrs
from pprint import pprint

api_instance = AMZ_attrs()

try:
    offset = 0
    limit = 10

    while True:
        res = api_instance.get_sub_attr_by_attr_code("1001", offset=offset, limit=limit)

        if limit > len(res):
            break
        else:
            offset = offset + limit

    pprint(res)

except Exception as e:
    print("Exception when calling get_sub_attr_by_attr_code %s\n" % e)