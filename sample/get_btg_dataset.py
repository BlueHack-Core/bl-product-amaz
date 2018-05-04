from __future__ import print_function
from  bl_product_amaz.us_btgs import US_btgs
from pprint import pprint

api_instance = US_btgs()

try:
    offset = 0
    limit = 100

    while True:
        res = api_instance.get_btg_dataset(offset=offset, limit=limit)

        if limit > len(res):
            break
        else:
            offset = offset + limit

    pprint(res)

except Exception as e:
    print("Exception when calling get_btg_dataset: %s\n" % e)