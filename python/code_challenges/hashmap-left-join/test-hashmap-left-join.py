import bytest
from hashmap-left-join.hashmap-left-join import HashTable, left_join_hash

def test_left_join_hash():
  ht_one = HashTable()
  ht_one.add("fond", "enamored")
  ht_one.add("wrath", "anger")
  ht_one.add("diligent", "employed")
  ht_one.add("outfit", "garb")
  ht_one.add("guide", "usher")
  ht_two = HashTable()
  ht_two.add("fond", "averse")
  ht_two.add("wrath", "delight")
  ht_two.add("diligent", "idle")
  ht_two.add("guide", "follow")
  ht_two.add("flow", "jam")
  assert (left_join_hash(ht_one,ht_two)) == [['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight'], ['outfit', 'garb', None], ['diligent', 'employed', 'idle'], ['flow', None, 'jam']]
