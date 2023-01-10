/* RAII
 * ======
 *
 * Variables in Rust do more than just hold data in the stack: they also -own- resources. e.g.
 * Box<T> owns memory in the heap. Rust enforces RAII (Resource Acquistion Is Initialization), so
 * whenever an object goes out of cope, its destructor is called and its owned resources are freed.
 *
 * This behavior shields against resource leak bugs, so you'll never have to manually free memory
 * or worry about memory leaks again! Here's a quick showcase: */

// raii.rs --?
fn create_box() {
    // Allocate an integer on the heap
    let _box1 = Box::new(3i32);

    // '_box1' is destroyed here, and memory gets freed
}

fn main() {
    // Allocate an integer on the heap
    let _box2 = Box::new(5i32);
     
    // A nested scope:
    {
        // Allocate an integer on the heap
        let _box3 = Box::new(4i32);

        // '_box3' is destroyed here, and memory gets freed
    }

    // Creating lots of boxes just for fun
    // There'as no need to manually free memory!
    for _ in 0u32..1_000 {
        create_box();
    }

    // '_box2' is destroyed here, and memory gets freed


    // ****
    let x = ToDrop;
    println!("Made a ToDrop!");
}

/* Destructor
 * ============
 *
 * The notion of a destructor in Rust is provided through the Drop trait. The destructor is called
 * when the resource goes out of scope. This trait is not required to be implemented for every
 * type, only implement it for your type if you require its own destructor logic. 
 *
 * Run the below exacmple to see how the Drop trait works. When the varialbe in the main function
 * goes out of scope the custom destructor will be invoked. 
 *
 * NB! **** will be but in above main() */

struct ToDrop;

impl Drop for ToDrop {
    fn drop(&mut self) {
        println!("ToDrop is being dropped");
    }
}

// I'm not really understanding whats happening with ToDrop. Its getting printed even if its not
// called..? 

