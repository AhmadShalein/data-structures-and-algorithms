def validate_brackets(input_brackets):
  open_list = ["(","[","{"]
  close_list = [")","]","}"]
  stack = []
  for i in input_brackets:
    if i in open_list:
      stack.append(i)
    elif i in close_list:
      pos = close_list.index(i)
      if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
        stack.pop()
      else:
        return False
  if len(stack) == 0:
    return True
  else:
    return False

if __name__=='__main__':
  string_one = "{[]{}}"
  print(validate_brackets(string_one))

  string_two = "{[][{}}"
  print(validate_brackets(string_two))
