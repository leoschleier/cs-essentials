use log::debug;

use cs_essentials::hash_table::HashTable;

fn main() {
    env_logger::init();
    debug!("Executing binary.");

    let mut my_hash_table = HashTable::<i32>::new();

    my_hash_table.add("my_key", 69);
    my_hash_table.add("my_second_key", 69_i32.pow(2));

    let my_fav_numb = my_hash_table.get("my_key");
    let my_second_fav_numb = my_hash_table.get("my_second_key");

    match my_fav_numb {
        Some(numb) => println!("My favorite number: {numb}"),
        _ => println!("Number not found."),
    }

    match my_second_fav_numb {
        Some(numb) => println!("My second favorite number: {numb}"),
        _ => println!("Number not found."),
    }
}
