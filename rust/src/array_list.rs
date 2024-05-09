const INIT_LEN: usize = 2;

struct ArrayList<A> {
    arr: A,
    length: usize,
}

enum Entry<T>{
    Null,
    Item(T),
}



impl<T, const N: usize> ArrayList<A> 
where T: Copy + Clone
{
    
    pub fn new() -> ArrayList<T, N> {
        ArrayList {
            arr: Box::new(create_empty_array::<T, N>()),
            length: 0,
        }
    }

    pub fn length(&self) -> usize {
        self.length
    }

    fn extend_size<const M: usize>(&mut self) {
        let new_arr = create_empty_array::<T, M>();
        
        for (i, val) in self.arr.iter().enumerate(){
            new_arr[i] = *val;
        }

        self.arr = Box::new(new_arr);

    }


}

fn create_empty_array<T: Copy, const N: usize>() -> [Entry<T>; N]{
    core::array::from_fn::<Entry<T>, N, _>(|_| Entry::Null)
}
