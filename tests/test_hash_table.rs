use cs_essentials::hash_table::HashTable;

#[test]
fn test_hash_table() {
    let key_values = [("my_fav_numb", 69), ("my_sec_fav_numb", 69_i32.pow(2))];

    let mut my_hash_table = HashTable::<i32>::new();

    // Add all key-value pairs to the hash table.
    for (key, value) in key_values {
        my_hash_table.add(key, value);
    }

    // Check all key-value pairs in the hash table.
    for (key, value) in key_values {
        match my_hash_table.get(key) {
            Some(result) => assert_eq!(
                result, &value,
                "Expected '{}' but got '{}'",
                value, result
            ),
            _ => assert!(false, "Expected 'Some' but received 'None'."),
        }
    }
}
