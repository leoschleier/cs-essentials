from typing import Any

from cs_essentials.arrays_strings import hash_table


def test_hash_table_str_key() -> None:
    ht = hash_table.HashTable[str, Any](100)
    ht.set("key1", "value1")
    ht.set("key2", "value2")
    assert ht.get("key1") == "value1"
    assert ht.get("key2") == "value2"


def test_hash_table_any_key() -> None:
    ht = hash_table.HashTable[Any, Any](100)
    ht.set(69, "value1")
    ht.set("mykey", "value2")
    ht.set(True, "value3")
    assert ht.get(69) == "value1"
    assert ht.get("mykey") == "value2"
    assert ht.get(True) == "value3"
