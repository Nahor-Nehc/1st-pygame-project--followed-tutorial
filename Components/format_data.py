def unformat_data(str_):
  str_ = str_.split(",")
  return [int(x) for x in str_]

def format_data(list_):
  return ",".join([str(x) for x in list_])

def convert(arg):
  if type(arg) == str:
    return unformat_data(arg)
  elif type(arg) == list:
    return format_data(arg)
  else:
    raise ValueError("Argument not string gor list type")