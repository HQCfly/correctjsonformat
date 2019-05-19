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

# performance testing
1. python -m cProfile no_corr_json.py 
```
80548 function calls (80394 primitive calls) in 0.357 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    19/18    0.000    0.000    0.011    0.001 <frozen importlib._bootstrap>:1009(_handle_fromlist)
       14    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:103(release)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:143(__init__)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:147(__enter__)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:151(__exit__)
       14    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:157(_get_module_lock)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:176(cb)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:194(_lock_unlock_module)
     16/3    0.000    0.000    0.062    0.021 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
      146    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:222(_verbose_message)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:307(__init__)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:311(__enter__)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:318(__exit__)
       48    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:321(<genexpr>)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:369(__init__)
       21    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:403(cached)
       14    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:416(parent)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:424(has_location)
       12    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:504(_init_module_attrs)
    12/10    0.000    0.000    0.031    0.003 <frozen importlib._bootstrap>:576(module_from_spec)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
     12/3    0.000    0.000    0.074    0.025 <frozen importlib._bootstrap>:663(_load_unlocked)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:719(find_spec)
       14    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:78(acquire)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:792(find_spec)
       36    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:855(__enter__)
       36    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:859(__exit__)
       12    0.000    0.000    0.004    0.000 <frozen importlib._bootstrap>:882(_find_spec)
     12/3    0.000    0.000    0.074    0.025 <frozen importlib._bootstrap>:948(_find_and_load_unlocked)
     12/3    0.000    0.000    0.075    0.025 <frozen importlib._bootstrap>:978(_find_and_load)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1029(__init__)
        3    0.000    0.000    0.030    0.010 <frozen importlib._bootstrap_external>:1040(create_module)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1048(exec_module)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1190(_path_hooks)
       33    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1203(_path_importer_cache)
       12    0.000    0.000    0.004    0.000 <frozen importlib._bootstrap_external>:1240(_get_spec)
       12    0.000    0.000    0.004    0.000 <frozen importlib._bootstrap_external>:1272(find_spec)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1319(__init__)
       16    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1325(<genexpr>)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1351(_get_spec)
       27    0.001    0.000    0.003    0.000 <frozen importlib._bootstrap_external>:1356(find_spec)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1404(_fill_cache)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1433(<setcomp>)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1445(path_hook_for_FileFinder)
       18    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:271(cache_from_source)
       27    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:36(_relax_case)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:369(_get_cached)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:401(_check_name_wrapper)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:438(_classify_pyc)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:471(_validate_timestamp_pyc)
       27    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:51(_r_long)
        9    0.000    0.000    0.004    0.000 <frozen importlib._bootstrap_external>:523(_compile_bytecode)
      133    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:56(_path_join)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:574(spec_from_file_location)
      133    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:58(<listcomp>)
       18    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:62(_path_split)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:719(create_module)
      9/3    0.000    0.000    0.073    0.024 <frozen importlib._bootstrap_external>:722(exec_module)
       53    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:74(_path_stat)
        9    0.000    0.000    0.028    0.003 <frozen importlib._bootstrap_external>:793(get_code)
       17    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:84(_path_is_mode_type)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:884(__init__)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:909(get_filename)
        9    0.001    0.000    0.023    0.003 <frozen importlib._bootstrap_external>:914(get_data)
       15    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:93(_path_isfile)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:951(path_stats)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:98(_path_isdir)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 <string>:1(__new__)
     5000    0.012    0.000    0.111    0.000 __init__.py:299(loads)
        3    0.000    0.000    0.001    0.000 __init__.py:316(namedtuple)
       12    0.000    0.000    0.000    0.000 __init__.py:388(<genexpr>)
        1    0.000    0.000    0.000    0.000 __init__.py:43(normalize_encoding)
        1    0.000    0.000    0.003    0.003 __init__.py:71(search_function)
        1    0.000    0.000    0.024    0.024 __init__.py:97(<module>)
        1    0.000    0.000    0.000    0.000 abc.py:1(<module>)
        6    0.000    0.000    0.000    0.000 abc.py:125(__new__)
        4    0.000    0.000    0.000    0.000 abc.py:130(register)
      8/4    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
       42    0.000    0.000    0.000    0.000 abc.py:7(abstractmethod)
        1    0.000    0.000    0.000    0.000 codecs.py:94(__new__)
        1    0.000    0.000    0.009    0.009 correctjson.py:1099(_make_unsafe_string_chars)
        1    0.000    0.000    0.000    0.000 correctjson.py:1102(<listcomp>)
        1    0.000    0.000    0.009    0.009 correctjson.py:1109(helpers)
        1    0.000    0.000    0.038    0.038 correctjson.py:118(<module>)
        1    0.001    0.001    0.001    0.001 correctjson.py:1587(position_marker)
        1    0.000    0.000    0.000    0.000 correctjson.py:164(_get_pyver)
        1    0.000    0.000    0.000    0.000 correctjson.py:1748(buffered_stream)
        1    0.000    0.000    0.000    0.000 correctjson.py:183(_dummy_context_manager)
        1    0.000    0.000    0.000    0.000 correctjson.py:186(__enter__)
        1    0.000    0.000    0.000    0.000 correctjson.py:189(__exit__)
        1    0.001    0.001    0.001    0.001 correctjson.py:212(determine_float_limits)
        1    0.000    0.000    0.000    0.000 correctjson.py:2167(JSONException)
        1    0.000    0.000    0.000    0.000 correctjson.py:2173(JSONSkipHook)
        1    0.000    0.000    0.000    0.000 correctjson.py:2182(JSONStopProcessing)
        1    0.000    0.000    0.000    0.000 correctjson.py:2191(JSONAbort)
        1    0.000    0.000    0.000    0.000 correctjson.py:2195(JSONError)
        1    0.000    0.000    0.000    0.000 correctjson.py:2309(JSONDecodeError)
        1    0.000    0.000    0.000    0.000 correctjson.py:2314(JSONDecodeHookError)
        1    0.000    0.000    0.000    0.000 correctjson.py:2334(JSONEncodeError)
        1    0.000    0.000    0.000    0.000 correctjson.py:2339(JSONEncodeHookError)
        1    0.000    0.000    0.000    0.000 correctjson.py:2363(encode_state)
        1    0.000    0.000    0.000    0.000 correctjson.py:2414(decode_statistics)
        1    0.000    0.000    0.000    0.000 correctjson.py:2548(decode_state)
       18    0.000    0.000    0.000    0.000 correctjson.py:268(<lambda>)
        1    0.000    0.000    0.000    0.000 correctjson.py:2800(_behaviors_metaclass)
        1    0.001    0.001    0.001    0.001 correctjson.py:2826(__new__)
        1    0.000    0.000    0.000    0.000 correctjson.py:2998(json_options)
        1    0.000    0.000    0.000    0.000 correctjson.py:3551(JSON)
        1    0.000    0.000    0.000    0.000 correctjson.py:370(_undefined_class)
        1    0.000    0.000    0.000    0.000 correctjson.py:399(_nonnumber_float_constants)
        1    0.000    0.000    0.000    0.000 correctjson.py:5968(jsonlint)
        1    0.000    0.000    0.000    0.000 correctjson.py:774(json_int)
        2    0.000    0.000    0.000    0.000 correctjson.py:872(_make_raw_bytes)
        1    0.000    0.000    0.000    0.000 correctjson.py:885(utf32)
        1    0.000    0.000    0.022    0.022 decimal.py:2(<module>)
        1    0.000    0.000    0.011    0.011 decoder.py:2(<module>)
        1    0.000    0.000    0.000    0.000 decoder.py:20(JSONDecodeError)
        1    0.000    0.000    0.000    0.000 decoder.py:254(JSONDecoder)
        1    0.005    0.005    0.005    0.005 decoder.py:284(__init__)
     5000    0.016    0.000    0.093    0.000 decoder.py:332(decode)
     5000    0.060    0.000    0.060    0.000 decoder.py:343(raw_decode)
        1    0.000    0.000    0.000    0.000 encoder.py:104(__init__)
        1    0.000    0.000    0.001    0.001 encoder.py:2(<module>)
        1    0.000    0.000    0.000    0.000 encoder.py:73(JSONEncoder)
       20    0.000    0.000    0.000    0.000 enum.py:283(__call__)
       20    0.000    0.000    0.000    0.000 enum.py:525(__new__)
       23    0.000    0.000    0.000    0.000 enum.py:620(name)
        5    0.000    0.000    0.000    0.000 enum.py:625(value)
        2    0.000    0.000    0.000    0.000 enum.py:790(_missing_)
        2    0.000    0.000    0.000    0.000 enum.py:797(_create_pseudo_member_)
        4    0.000    0.000    0.000    0.000 enum.py:827(__or__)
        6    0.000    0.000    0.000    0.000 enum.py:833(__and__)
        3    0.000    0.000    0.000    0.000 enum.py:852(_high_bit)
        2    0.000    0.000    0.000    0.000 enum.py:869(_decompose)
        2    0.000    0.000    0.000    0.000 enum.py:887(<listcomp>)
        5    0.000    0.000    0.000    0.000 enum.py:898(<lambda>)
        5    0.000    0.000    0.000    0.000 enum.py:904(_power_of_two)
        1    0.036    0.036    0.357    0.357 no_corr_json.py:1(<module>)
     4999    0.002    0.000    0.002    0.000 no_corr_json.py:11(dict_generator)
     5000    0.005    0.000    0.029    0.000 no_corr_json.py:50(trans_hex_chinese)
        1    0.000    0.000    0.000    0.000 numbers.py:12(Number)
        1    0.000    0.000    0.000    0.000 numbers.py:147(Real)
        1    0.000    0.000    0.000    0.000 numbers.py:267(Rational)
        1    0.000    0.000    0.000    0.000 numbers.py:294(Integral)
        1    0.000    0.000    0.000    0.000 numbers.py:32(Complex)
        1    0.000    0.000    0.001    0.001 numbers.py:6(<module>)
        1    0.000    0.000    0.000    0.000 raw_unicode_escape.py:13(Codec)
        1    0.000    0.000    0.000    0.000 raw_unicode_escape.py:20(IncrementalEncoder)
        1    0.000    0.000    0.000    0.000 raw_unicode_escape.py:24(IncrementalDecoder)
        1    0.000    0.000    0.000    0.000 raw_unicode_escape.py:28(StreamWriter)
        1    0.000    0.000    0.000    0.000 raw_unicode_escape.py:31(StreamReader)
        1    0.000    0.000    0.000    0.000 raw_unicode_escape.py:36(getregentry)
        1    0.000    0.000    0.000    0.000 raw_unicode_escape.py:8(<module>)
        6    0.000    0.000    0.003    0.001 re.py:232(compile)
        6    0.000    0.000    0.003    0.001 re.py:271(_compile)
        1    0.000    0.000    0.007    0.007 scanner.py:2(<module>)
       14    0.000    0.000    0.000    0.000 sre_compile.py:249(_compile_charset)
       14    0.000    0.000    0.000    0.000 sre_compile.py:276(_optimize_charset)
        4    0.000    0.000    0.000    0.000 sre_compile.py:411(_mk_bitmap)
        4    0.000    0.000    0.000    0.000 sre_compile.py:413(<listcomp>)
        9    0.000    0.000    0.000    0.000 sre_compile.py:423(_simple)
       13    0.000    0.000    0.000    0.000 sre_compile.py:453(_get_iscased)
      8/5    0.000    0.000    0.000    0.000 sre_compile.py:461(_get_literal_prefix)
        5    0.000    0.000    0.000    0.000 sre_compile.py:492(_get_charset_prefix)
        6    0.000    0.000    0.000    0.000 sre_compile.py:536(_compile_info)
       12    0.000    0.000    0.000    0.000 sre_compile.py:595(isstring)
        6    0.000    0.000    0.001    0.000 sre_compile.py:598(_code)
       12    0.000    0.000    0.000    0.000 sre_compile.py:65(_combine_flags)
     25/6    0.000    0.000    0.001    0.000 sre_compile.py:71(_compile)
        6    0.000    0.000    0.003    0.000 sre_compile.py:759(compile)
       26    0.000    0.000    0.000    0.000 sre_parse.py:111(__init__)
       52    0.000    0.000    0.000    0.000 sre_parse.py:160(__len__)
      123    0.000    0.000    0.000    0.000 sre_parse.py:164(__getitem__)
       10    0.000    0.000    0.000    0.000 sre_parse.py:168(__setitem__)
       25    0.000    0.000    0.000    0.000 sre_parse.py:172(append)
    31/12    0.000    0.000    0.000    0.000 sre_parse.py:174(getwidth)
        6    0.000    0.000    0.000    0.000 sre_parse.py:224(__init__)
      102    0.000    0.000    0.000    0.000 sre_parse.py:233(__next)
       71    0.000    0.000    0.000    0.000 sre_parse.py:249(match)
       71    0.000    0.000    0.000    0.000 sre_parse.py:254(get)
        4    0.000    0.000    0.000    0.000 sre_parse.py:258(getwhile)
       38    0.000    0.000    0.000    0.000 sre_parse.py:286(tell)
       16    0.000    0.000    0.000    0.000 sre_parse.py:295(_class_escape)
        4    0.000    0.000    0.000    0.000 sre_parse.py:343(_escape)
        9    0.000    0.000    0.000    0.000 sre_parse.py:408(_uniq)
     13/6    0.000    0.000    0.002    0.000 sre_parse.py:417(_parse_sub)
     15/6    0.001    0.000    0.002    0.000 sre_parse.py:475(_parse)
        6    0.000    0.000    0.000    0.000 sre_parse.py:76(__init__)
       24    0.000    0.000    0.000    0.000 sre_parse.py:81(groups)
        6    0.000    0.000    0.000    0.000 sre_parse.py:84(opengroup)
        6    0.000    0.000    0.000    0.000 sre_parse.py:903(fix_flags)
        6    0.000    0.000    0.002    0.000 sre_parse.py:919(parse)
        6    0.000    0.000    0.000    0.000 sre_parse.py:96(closegroup)
       28    0.000    0.000    0.000    0.000 types.py:164(__get__)
       12    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x1009449e0}
        6    0.000    0.000    0.000    0.000 {built-in method _abc._abc_init}
        4    0.000    0.000    0.000    0.000 {built-in method _abc._abc_register}
      8/4    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        9    0.000    0.000    0.000    0.000 {built-in method _imp._fix_co_filename}
       62    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
        3    0.022    0.007    0.030    0.010 {built-in method _imp.create_dynamic}
        3    0.000    0.000    0.000    0.000 {built-in method _imp.exec_dynamic}
        7    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
       12    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
       62    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        6    0.000    0.000    0.000    0.000 {built-in method _sre.compile}
       24    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
       28    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
       36    0.001    0.000    0.012    0.000 {built-in method builtins.__build_class__}
        2    0.000    0.000    0.013    0.006 {built-in method builtins.__import__}
       12    0.000    0.000    0.000    0.000 {built-in method builtins.any}
      288    0.000    0.000    0.000    0.000 {built-in method builtins.chr}
     13/1    0.001    0.000    0.357    0.357 {built-in method builtins.exec}
       72    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
       73    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
     5224    0.002    0.000    0.002    0.000 {built-in method builtins.isinstance}
5349/5321    0.002    0.000    0.002    0.000 {built-in method builtins.len}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.max}
       59    0.000    0.000    0.000    0.000 {built-in method builtins.min}
       17    0.000    0.000    0.000    0.000 {built-in method builtins.ord}
     5000    0.107    0.000    0.107    0.000 {built-in method builtins.print}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.repr}
        5    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
       27    0.000    0.000    0.000    0.000 {built-in method from_bytes}
        9    0.004    0.000    0.004    0.000 {built-in method marshal.loads}
       30    0.000    0.000    0.000    0.000 {built-in method posix.fspath}
        7    0.001    0.000    0.001    0.000 {built-in method posix.getcwd}
        2    0.000    0.000    0.000    0.000 {built-in method posix.listdir}
       53    0.001    0.000    0.001    0.000 {built-in method posix.stat}
        3    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
        3    0.000    0.000    0.000    0.000 {built-in method sys.intern}
      254    0.004    0.000    0.004    0.000 {built-in method unicodedata.category}
       12    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        9    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
      398    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        3    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
       81    0.000    0.000    0.000    0.000 {method 'capitalize' of 'str' objects}
     5000    0.008    0.000    0.008    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     5000    0.013    0.000    0.016    0.000 {method 'encode' of 'str' objects}
    10000    0.002    0.000    0.002    0.000 {method 'end' of 're.Match' objects}
       15    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
       15    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
       48    0.000    0.000    0.000    0.000 {method 'find' of 'bytearray' objects}
       33    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
       60    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
       18    0.000    0.000    0.000    0.000 {method 'isalnum' of 'str' objects}
       23    0.000    0.000    0.000    0.000 {method 'isdigit' of 'str' objects}
       12    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        8    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
      156    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        9    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
    10000    0.014    0.000    0.014    0.000 {method 'match' of 're.Pattern' objects}
        9    0.022    0.002    0.022    0.002 {method 'read' of '_io.FileIO' objects}
        5    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
       91    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
      284    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
       34    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        7    0.000    0.000    0.000    0.000 {method 'setter' of 'property' objects}
        2    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
     5013    0.004    0.000    0.004    0.000 {method 'startswith' of 'str' objects}
        4    0.000    0.000    0.000    0.000 {method 'translate' of 'bytearray' objects}
```
The specific explanations for each column output are as follows:：

●ncalls：Represents the number of function calls；

●tottime：Represents the total run time of the specified function, removing the running time of the child function called in the function；

●percall：(the first percall) is equal to tottime/ncalls；

●cumtime：Indicates the time when the function and all its subfunctions are called to run, that is, when the function starts calling to return.；

●percall：(the second percall) is the average time it takes a function to run once, equal to cumtime/ncalls；

●filename:lineno(function)：Specific information for each function call

Comparison between the three: profile is very slow and can only be used for some small script tests. 
Testing larger benchmark often takes more than ten minutes or more. Hotshot and cProfile are implemented in C. So itundefineds faster. 
Hotshot has a disadvantage that it doesnundefinedt support multithreaded programming, and itundefineds no longer maintained after python2.5, 
and the newer version no longer supports. CProfile is faster and more applicable than the other two.
2. python -m cProfile -o no_corr_json.pstats no_corr_json.py
python gprof2dot.py -f pstats no_corr_json.pstats | dot -Tpng -o no_corr_json.png
![Image](https://github.com/HQCfly/correctjsonformat/blob/master/no_corr__results.png)
