/* OK just gonna repeat this as a small example in here, as I think this can be valuable to learn
 * more about lifetimes etc. */

struct Droppable {
    name: &'static str,
}

impl Drop for Droppable {           // So I guess Trait Drop is in the standard library 
    fn drop(&mut self) {
        println!("> Dropping {}", self.name);   // This interestingly get executed as soon as a
                                                // variable goes out of scope or loosing its
                                                // lifetime I guess? 
    }
}


fn main() {
   let _outer_scope = Droppable { name: "outer" };

   {
       let _middle_one = Droppable { name: "middle_one" };
       let _middle_two = Droppable { name: "middle_two" };

       {
           let _inner_most = Droppable { name: "inner" };

           println!("Exiting the inner scope");
       }
       println!("Exited the inner scope\n");
       println!("Exiting the middle scope");
   }
   println!("Exited the middle scope. Now in the outer scope\n");
   
   // Manually dropping the outer scope variable
   drop(_outer_scope);       // Notice its a own thing, not the the same i impl above? or? 

   println!("Manually dropped outer_scope above\n");
   println!("Done, exiting the program\n");
}
