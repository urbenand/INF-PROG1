# This one is the same as e04, but with ahv number as key

import p04_helpers as helper
import json

# collect data, False means, we collect multiple data
data_set = helper.collect_data(False)

# print pretty data by using json.dumps()
print(json.dumps(data_set, sort_keys=False, indent=4))
