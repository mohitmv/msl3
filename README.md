Welcome to msl
===================


`msl` is a collections of simple and natural functions, extending python's inbuilt functions.
Best and suggested way to use msl: 
<kbd><b>from msl import *</b></kbd>

----------



Methods for `msl-1.0.0`
-------------

### 
Method   | Short Description
-------- | ---
id_func(x) | return the input itself.
get_first(x, y) |return the first argument from first two inputs.
get_second(x, y) | return the second argument from first two inputs.
get_last(*args) | return the last argument. 
get_keys( obj )  | returns the keys of key-value-pairing obj.
get_keys_values(&nbsp;obj&nbsp;) | Return the List of (key, value) of key-value-pairing obj.
get_values( obj ) | Return the List of value of key-value-pairing obj.
has_key(obj, key) | Return True iff obj[key] is defined.
has_keys(obj, keys) | Return True iff all keys are defined.
run_func(func,&nbsp;*args) | operates func on args considering first few arguments as per need of func.
left_fold( ... ) | operates left_fold on array.
mapped( ... ) | Return key-value-pairing object of array’s type but mapped (new_key, new_value) pairs.
const_func( obj ) | Return a func which always returns obj
get_value( ... ) | Let key_sequence = [ k0, k1, k2 ], returns obj[k0][k1][k2] if defined else return default_value.
none_default( ... ) | Wrapper to replace None objects with some default object. 


----------


### Detailed Documentation

**get_keys( obj )**
 - Input Assertion - obj must be key-value-pairing object.
 - returns [0,1,2,3] if obj was list of size 4.

**get_keys_values( obj )**
 - Input Assertion - obj must be key-value-pairing object.
 - Return the List of (key, value) of key-value-pairing obj.

**get_values( obj )**
 - Input Assertion - obj must be key-value-pairing object.
 - Return the List of value of key-value-pairing obj.

**has_key(obj, key)**
 - Input Assertion - obj must be key-value-pairing object
 - Return True iff obj[key] is defined.

**has_keys(obj, keys)**
 - Input assertions - obj must be key-value-pairing objects, keys must be list of keys.
 - Return True iff all keys are defined.

run_func( func, *args )
: Input Assertion - func must be valid python func.
operates func on args considering first few arguments as per need of func. Will ignore extra arguments, will add “None” if there are less arguments. 
Warning: Don’t use it for func having *, ** or default arguments.

left_fold(func, array, id_element)
: Input Assertion - 
&nbsp;&nbsp; 1. Func must be valid python func.
&nbsp;&nbsp; 2. array must be key-value pairing object.
: operates left_fold on array.

mapped( func=None, array, filtering_func=None, key_func=None )
: Input Acceptance - None replacer
1. filtering_func = const_func( True )
2. key_func = id_func
3. func = id_func
: Input assertion
1. Func, filtering_func, key_func must be valid python func.
2. Array must be valid key-value-pairing object.
: Return key-value-pairing object of array’s type but mapped (new_key, new_value) pairs.
1. new_key = key_func(old_key, old_value)
2. new_value = func(old_value, old_key)
3. keeps a pair iff filtering_func(old_value, old_key) is True 


get_value(obj, key_sequence, default_value = None)
: Input assertion - 
1. Key_sequence must be list of keys.
2. Let key_sequence = [ k0, k1, k2 ], each of obj, obj[k0], obj[k0][k1] must be key-value-pairing object or undefined.
: Let key_sequence = [ k0, k1, k2 ], returns obj[k0][k1][k2] if defined else return default_value.


none_default( obj, default_value, func=None, none=None, none_func=None )
: Input Acceptance - Replace None by id_func for “func”, “none_func” operators.
: Input Assertions
1. func, none_func must be callable objects ( like python functions ) 
: Wrapper to replace None objects with some default object. 


----------

