# INTEGER (Numeric Types) #
data_integer = 7
print("data : ", data_integer, ", is an : ", type(data_integer), "type") # check #
# -- or --
data_integer = int(7)
print("data : ", data_integer, ", is an : ", type(data_integer), "type") # check #

# FLOAT (Numeric Types) #
data_float = 23.5
print("data : ", data_float, ", is an : ", type(data_float), "type") # check #
# -- or --
data_float = float(23.5)
print("data : ", data_float, ", is an : ", type(data_float), "type") # check #

# COMPLEX (Numeric Types) #
data_complex = 7j
print("data : ", data_complex, ", is an : ", type(data_complex), "type") # check #
# -- or --
data_complex = complex(7, 8)
print("data : ", data_complex, ", is an : ", type(data_complex), "type") # check #

# STRING (Text Type) #
data_string = "Heejin"
print("data : ", data_string, ", is an : ", type(data_string), "type") # check #
# -- or --
data_string = str("Heejin")
print("data : ", data_string, ", is an : ", type(data_string), "type") # check #

# BOOLEAN (Boolean Type) #
data_boolean = True
print("data : ", data_boolean, ", is an : ", type(data_boolean), "type") # check #
data_boolean = False
print("data : ", data_boolean, ", is an : ", type(data_boolean), "type") # check #
# -- or --
data_boolean = bool(23)
print("data : ", data_boolean, ", is an : ", type(data_boolean), "type") # check #

# C LANGUAGE #
from ctypes import c_double
data_c_double = c_double(11.5)
print("data : ", data_c_double, ", is an : ", type(data_c_double), "type") # check #

# LIST (Sequence Types) #
data_list = ["car", "bike", "bus"]
print("data : ", data_list, ", is an : ", type(data_list), "type") # check #
# -- or --
data_list = list(("car", "bike", "bus"))
print("data : ", data_list, ", is an : ", type(data_list), "type") # check #

# TUPLE (Sequence Types) #
data_tuple = ("Arsenal", "Chelsea", "Liverpool")
print("data : ", data_tuple, ", is an : ", type(data_tuple), "type") # check #
# -- or --
data_tuple = tuple(("Arsenal", "Chelsea", "Liverpool"))
print("data : ", data_tuple, ", is an : ", type(data_tuple), "type") # check #

# RANGE (Sequence Types) #
data_range = range(17)
print("data : ", data_range, ", is an : ", type(data_range), "type") # check #

# DICT (Mapping Type) #
data_dict = {"name" : "Yves", "age" : 24}
print("data : ", data_dict, ", is an : ", type(data_dict), "type") # check #
# -- or --
data_dict = dict(name="Yves", age=24)
print("data : ", data_dict, ", is an : ", type(data_dict), "type") # check #

# SET (Set Types) #
data_set = {"cat", "dog", "bird"}
print("data : ", data_set, ", is an : ", type(data_set), "type") # check #
# -- or --
data_set = set(("cat", "dog", "bird"))
print("data : ", data_set, ", is an : ", type(data_set), "type") # check #

# FROZENSET (Set Types) #
data_frozenset = frozenset({"football", "basketball", "badminton"})
print("data : ", data_frozenset, ", is an : ", type(data_frozenset), "type") # check #
# -- or --
data_frozenset = frozenset(("football", "basketball", "badminton"))
print("data : ", data_frozenset, ", is an : ", type(data_frozenset), "type") # check #

# BYTES (Binary Types) #
data_bytes = b"Morning"
print("data : ", data_bytes, ", is an : ", type(data_bytes), "type") # check #
# -- or --
data_bytes = bytes(18)
print("data : ", data_bytes, ", is an : ", type(data_bytes), "type") # check #

# BYTEARRAY (Binary Types) #
data_bytearray = bytearray(87)
print("data : ", data_bytearray, ", is an : ", type(data_bytearray), "type") # check #

# MEMORYVIEW (Binary Types) #
data_memoryview = memoryview(bytes(3))
print("data : ", data_memoryview, ", is an : ", type(data_memoryview), "type") # check #