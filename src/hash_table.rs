use log::debug;

#[derive(PartialEq, Debug)]
struct Node<T> {
    value: T,
    next: Box<LinkedList<T>>,
}

#[derive(PartialEq, Debug)]
struct KeyValue<T> {
    key: Box<str>,
    value: T,
}

#[derive(PartialEq, Debug)]
enum LinkedList<T> {
    Null,
    Node(Node<T>),
}

const TABLE_LEN: usize = 10;
const TABLE_LEN_U64: u64 = TABLE_LEN as u64;

#[derive(Debug)]
pub struct HashTable<T> {
    arr: [LinkedList<KeyValue<T>>; TABLE_LEN],
}

impl<T: std::cmp::PartialEq> HashTable<T> {
    /// Create a new `HashTable`.
    pub fn new() -> Self {
        HashTable {
            arr: core::array::from_fn::<LinkedList<KeyValue<T>>, TABLE_LEN, _>(
                |_| LinkedList::Null,
            ),
        }
    }

    /// Add a key-value pair to the `HahTable`.
    pub fn add(&mut self, key: &str, value: T) {
        let index = HashTable::<T>::get_index(key);
        debug!("Add at index {index}.");

        let mut linked_list = &mut self.arr[index];

        match linked_list {
            // If first node is Null --> add first node with value at index and return
            LinkedList::Null => {
                *linked_list = LinkedList::Node(
                    HashTable::<T>::create_tail_node(key, value),
                );
                return;
            }
            _ => (),
        }

        // Iterate over nodes in LinkedList
        while let LinkedList::Node(ref mut node) = linked_list {
            if *node.value.key == *key {
                // If key == key --> replace value and retrun
                debug!("Matching key found. Replace existing");
                node.value.value = value;
                break;
            }
            if *node.next == LinkedList::Null {
                // If at the end of LinkedList --> Append new node
                debug!("Reached end. Add new node.");
                node.next = Box::new(LinkedList::Node(
                    HashTable::<T>::create_tail_node(key, value),
                ));
                break;
            }

            // Continue
            debug!("Continue.");
            linked_list = &mut *node.next;
        }
    }

    /// Get the value for a given key.
    pub fn get(&self, key: &str) -> Option<&T> {
        let index = HashTable::<T>::get_index(key);
        debug!("Look up at index {index}.");

        let mut linked_list = &self.arr[index];

        //Iterate over nodes in LinkedList
        while let LinkedList::Node(node) = linked_list {
            debug!("Current key: {:?}.", node.value.key);
            if *node.value.key == *key {
                // If key == key --> return value
                debug!("Matching key found.");
                return Some(&node.value.value);
            }

            // Continue
            debug!("Continue.");
            linked_list = &*node.next;
        }

        // If key not contained in `HashTable` --> return None
        None
    }

    fn create_tail_node(key: &str, value: T) -> Node<KeyValue<T>> {
        let node = Node {
            value: KeyValue {
                key: key.into(),
                value,
            },
            next: Box::new(LinkedList::Null),
        };

        node
    }

    /// Compute index for a string in the internal array by using a hash function.
    fn get_index(s: &str) -> usize {
        (fnv_1(s.as_bytes()) % TABLE_LEN_U64) as usize
    }
}

const FNV_OFFSET_BASIS: u64 = 14695981039346656037;
const FNV_PRIME: u64 = 1099511628211;

/// Compute the hash of a bytes array by using the Fowler-Noll-Vo hash function.
/// See: https://en.wikipedia.org/wiki/Fowler–Noll–Vo_hash_function
fn fnv_1(bytes: &[u8]) -> u64 {
    let mut hash = FNV_OFFSET_BASIS;
    for byte in bytes {
        hash = (hash as u128 * FNV_PRIME as u128) as u64;
        hash = hash ^ (*byte as u64);
    }

    hash
}
