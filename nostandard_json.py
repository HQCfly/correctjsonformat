import json
import correctjson
"""
1. Use trans_hex_chinese function to escape Chinese
2. Automatic Detection and automatic Correction of json format using demjson
3. Using json.dumps to convert corrected dict data to json format
4. If you want to expand nesting json data, 
   you first need to use json.loads to convert json data to dict data, 
   and then call the dict_generator function
"""
def dict_generator(indict, pre=None,depth=None):
    pre = pre[:] if pre else []
    if depth is None: depth=1
    if isinstance(indict, dict):
        for key, value in indict.items():
            if depth>1:
                if isinstance(value, dict):
                    if len(value) == 0:
                        yield pre+[key, '{}']
                    else:
                        for d in dict_generator(value, pre + [key],depth=depth-1):
                            yield d
                elif isinstance(value, list):
                    if len(value) == 0:
                        yield pre+[key, '[]']
                    else:
                        for v in value:
                            for d in dict_generator(v, pre + [key],depth=depth-1):
                                yield d
                elif isinstance(value, tuple):
                    if len(value) == 0:
                        yield pre+[key, '()']
                    else:
                        for v in value:
                            for d in dict_generator(v, pre + [key],depth=depth-1):
                                yield d
                else:
                    yield pre + [key, value]
            else:
                yield pre + [key, value]
    else:
        yield indict
def show_composite_dict(composite_json):
    for i in  composite_json:
        composite_key = '.'.join(i[0:-1])
        composite_value = i[-1]
        result_json = str(composite_key) + ":" + str(composite_value)
        print(result_json)

def trans_hex_chinese(hex_json):
    hex_encode = hex_json.encode('raw_unicode_escape')
    chinese_json = hex_encode.decode()
    return chinese_json

# for i in range(5000):
test_json = """{"name":"\x6F"，"chart":\"label\","myfriend":"\xE6\x9F\xB3\xE4\xBA\x91","number":"10.11.12.12","radix":-12,"URL":"Http://gkate.com","remote_addr":application/json;charset=utf-8,"number-two":"22.11.12.12","day1":{"day1-1":'alex',"day1-2":[1,3,2],"day1-3":"gkate","day1-4":{"day4":15,"day5":16}},"ip":hostname}"""
# 1
chinese_json = trans_hex_chinese(test_json)
# 2
correct_json = correctjson.decode(chinese_json)
s_josn = json.dumps(correct_json)
# 3
indict_json = json.loads(s_josn)
composite_json = dict_generator(indict_json)
show_composite_dict(composite_json)

# for i in composite_json:
#     print('.'.join(i[0:-1]),':',i[-1])