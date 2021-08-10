def test_validate_brackets_first():
  string = "{[]{()}}"
  expected = True
  actual = validate_brackets(string)
  assert expected == actual
  
def test_validate_brackets_second():
  string = "[{}{})(]"
  expected = False
  actual = validate_brackets(string)
  assert expected == actual
  
def test_validate_brackets_therd():
  string = "((()"
  expected = False
  actual = validate_brackets(string)
  assert expected == actual
