def format_name(f_name, l_name):
  """ Take first and last name and makes it Title"""
  f_name = f_name.title()
  l_name = l_name.title()
  #print(f_name , l_name)
  return f"{f_name} {l_name}"
result = format_name("john", "QOSIMI")
print(result)


