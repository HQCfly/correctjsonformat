# 通过json数据校验方法解决如下几个问题(CN)：

1.数据没有校验，系统处于裸奔状态，导致后期维护成本高；
2.编写一堆校验代码，混杂在业务代码中，导致代码可读性降低；
3.API交付的时候提供一大段接口描述文档，但用户还是要揣测文档意思。
4.自动校验json格式
5.自动纠正json错误格式
6.对于多层嵌套问题进行深入探讨
7.对于array拆分展开
8.特殊字符处理

# 使用方式
1. 使用transhex_chinese函数来转义汉语
2. correstjson自动检测和自动校正json格式。
3. 使用json.dump将校正后的dict数据转换为json格式
4. 如果要展开嵌套json数据，首先需要使用json.load将json数据转换为dict数据，然后调用dict_generator函数

# The following problems are solved by json data verification method.
	
1. The data is not checked and the system is running naked, which leads to the high cost of maintenance in the later stage. 
2. Write a bunch of check code, mixed with business code, resulting in less readability of the code; 
3.API delivery provides a large number of interface description documents, but users still have to speculate on the meaning of the document. 
4. Automatic check json format 
5. Automatically correct json error format 
6. The problem of multi-layer nesting is discussed in detail. 
7. For array split expansion. 
8. Special character processing

# Using steps
1. Use trans_hex_chinese function to escape Chinese
2. Automatic Detection and automatic Correction of json format using demjson
3. Using json.dumps to convert corrected dict data to json format
4. If you want to expand nesting json data, 
   you first need to use json.loads to convert json data to dict data, 
   and then call the dict_generator function

