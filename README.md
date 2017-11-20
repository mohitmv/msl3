Welcome to msl
===================


`msl` is a collections of simple and natural functions, extending python's inbuilt functions.
Best and suggested way to use msl: 
<kbd><b>from msl import *</b></kbd>

----------


**Warning:** `This document is incomplete and ill presented. email mohitsaini1196@gmail.com for more details.`

-------------


Definitions
----------

**Object**
 - ::= Atomic_Object  |  List of Objects  |  Dict_Object  |  Func  |  Class_Object

**Atomic_Object**
 - Objects which aren’t dependent on other objects. They have their independent life. Their state data is copied when assigned to new variable.
 - Example: Int, String, Bool, “None”


**Dict_Object**
 - An object storing List of (key, Object) with unique keys, offering access to sub-objects by corresponding key. 

**Key**
 - A string ( Sometime Integer ), used to access sub-objects of a 


**Func**
 - A function having Inputs, instructions and output
 - Alias - Operator

**Method**
 - A func offered by some object as key is called method.
 - Example: append method offered by list objects.


**Class_Object**
 - A black box offering sub-objects as keys, accessed by "." operator
 - All Objects are inherited from class_object originally.


**Arguments**
 - Alias for func inputs


**key-value-pairing object**
 - List of object | Dict of object | Pseudo Dict


**Pseudo xxxx**
 - An Class_Object which offer xxxx type interface but not a list actually. 
 - Example Pseudo List, Pseudo Dict etc
 
**Pseudo Dict**
 - An object storing (key, value) pairs. Maintaining unique keys, allowing to access values on a key.
 - Having .keys( ) method to return list of all keys.
 - Having .pop( ) method to remove a key.
 - Having .has_key( ) method to check if a key exists.


**Pure xxxx**
 - Sometime we call “pure xxxx” to “non pseudo xxxx” objects. Example pure list.


-------------


Knowledges
-------------
 - left_fold (func, array, identity_element) = o6(o3(o1(identity_element )))
    - Assuming array was [1, 3, 6] 
    - Where unary operator o_i = func(... , value, key); corresponding to i’th index in key-value-pairing object array.






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

<b>run_func( func, *args )</b>
 - Input Assertion - func must be valid python func.
 - operates func on args considering first few arguments as per need of func. Will ignore extra arguments, will add "None" if there are less arguments. 
 - Warning: Don’t use it for func having *, ** or default arguments.


**left_fold(func, array, id_element)**
 - Input Assertion - 
    - func must be valid python func.
    - Array must be key-value pairing object.
 - operates left_fold on array.

**mapped( func=None, array, filtering_func=None, key_func=None )**
 - Input Acceptance - None replacer
    - filtering_func = const_func( True )
    - key_func = id_func
    - func = id_func
 - Input assertion
    - Func, filtering_func, key_func must be valid python func.
    - Array must be valid key-value-pairing object.
 - Return key-value-pairing object of array’s type but mapped (new_key, new_value) pairs.
    - new_key = key_func(old_key, old_value)
    - new_value = func(old_value, old_key)
    - keeps a pair iff filtering_func(old_value, old_key) is True 


**get_value(obj, key_sequence, default_value = None)**
 - Input assertion - 
    - Key_sequence must be list of keys.
    - Let key_sequence = [ k0, k1, k2 ], each of obj, obj[k0], obj[k0][k1] must be key-value-pairing object or undefined.
 - Let key_sequence = [ k0, k1, k2 ], returns obj[k0][k1][k2] if defined else return default_value.


**none_default( obj, default_value, func=None, none=None, none_func=None )**
 - Input Acceptance - Replace None by id_func for “func”, “none_func” operators.
 - Input Assertions
    - func, none_func must be callable objects ( like python functions ) 
 - Wrapper to replace None objects with some default object. 


----------

