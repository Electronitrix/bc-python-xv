def reverse_string(string):
  if len(string) is 0:
    return None

  
  reversed_string = ""
  for index in range(len(string) - 1, 0, -1):
    reversed_string += string[index]

  if reversed_string == string:
    return True
  else:
    return reversed_string
print(reverse_string("solomon"))
print (reverse_string("misc"))