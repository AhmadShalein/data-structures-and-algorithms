import bytest
from hash-table.hash-table import HashTable

def test-hash-function():
  hash_table = HashTable()
  assert hash_table.add('hello') == 523
  
def test_add_item():
  hash_table = HashTable()
  hash_table.add('hello',15)
  assert len(hash_table.arr[hash_table.get_hash('hello')]) == 1
  
def test_get_item():
  hash_table = HashTable()
  hash_table.add('hello',15)
  assert hash_table.get('hello') == 15

def test_contains_item():
  hash_table = HashTable()
  hash_table.add('hello',15)
  assert table.contains('hello')

def test_delete_item():
  hash_table = HashTable()
  hash_table.add('hello',15)
  hash_table.delete('hello')
  assert len(hash_table.arr[hash_table.get_hash('hello')]) == 0
