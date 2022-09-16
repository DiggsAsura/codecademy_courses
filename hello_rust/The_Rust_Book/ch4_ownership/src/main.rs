// Starting the next big chapter in the rust-book
// https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html

fn main() {
    println!("The Stack and the Heap");
    println!("------------------------\n");

    // STACK
    println!("The stack stores values in the order it gets them and removes the values in the opposite order.");
    println!("This is referred to as \"last in, first out\"");

    println!("STACK = Plates");
    println!("When you add more plates, you puth them on top of the pile, and when you need a plate, you take one off the top.");
    // good one!

    println!("\nAdding data is called pushing onto the stack, and removing data is called popping off the stack.");
    println!("All data stored on the stack must have a known, fixed size!");
    println!("Data with unkown seize at compile time or a size that might change must be stored on the heap instead.\n");

    // OK sooo, how do I tell rust to store on stack vs heap?
    

    // HEAP
    println!("The heap is less orgainized. When you place stuff on the heap, you request a certain amount of space,");
    println!("then the memory allocator finds an empty spot in the heap at the right size, marks it as being used, and");
    println!("returns a pointer - which is the address of that location.");
    println!("This process is called allocating on the heap, and is sometimes abbreviated as just allocating (pushing)");
    println!("values onto the stack is not considered allocating). Because the pointer to the heap is a known, fixed size, you can");
    println!("store the pointer on the stack, but when you want the actual data, you must follow the pointer");
    // Resturant
    println!("Thik of being seated at a resturant!");
    println!("When you enter, you state the number of people in your group, and the staff finds an empty table that fits everyone and leads you there.");
    println!("If someone in your group comes late, they can ask where you've been seated to find you.\n");
    // good stuff again.
    

    // HEAP VS STACK
    println!("Accessing data in the heap is slower than the stack because you have to follow a pointer to get there");
    println!("Contemporary (modern) processors are faster if they jump around less in memory.\n");

    // Sum it up
    println!("Summary:");
    println!("When your code calls a function, the values passed into the function (including, potentially, pointers to data on the heap) and the function's local variables get pushed onto the stack.");
    println!("When the function is over, those values get popped off the stack.\n");

    println!("Keeping track of what parts of code are using what data on the heap, minimizing the amount of");
    println!("duplicate data on the heap, and cleaning up unused data on the heap so you don't run out of");
    println!("space are all problems that ownership addresses. Once you understand ownership, you won't need to think");
    println!("about the stack and the heap very often, but knowing that the main purpose of ownership is to");
    println!("manage heap data can explain why it works the way it does");
    println!("");


    // ****

    // Ownership Rules
    println!("* Each value in Rust has an owner");
    println!("* There can only be one owner at the time");
    println!("* When the owner goes out of scope, the value will be dropped");
    println!("");

    
    // Variable Scope
    // -----------------
    let s = "hello from outside";

    // The variable s refers to a string literal, where the value of the string is hardcoded
    // into the text of our program. The variable is valid from the point at which it's 
    // declared until the end of the current scope. Listing 4-1 shows a program with comments
    // annotating where the variable s would be valid.

    {                     // s is not valid here, it's not yet declared
        let s = "hello from inside";  // s is valid from this point forward
        println!("{s}");
        // do stuff with s

    }                     // this scope is now over, and s is no longer valid
    println!("{s}");


    // So this is similar to Python and other programming languages where stuff is not
    // accessible outside of scope. 
    // Now we'll build on top of this understanding by introducing the String type.


    // **
    // THE STRING TYPE
    // ****
    // 
    // The types covered previously in "Data Types" chapter, is all known size, and 
    // stored on the stack. We want to look at more complex data types stored on the 
    // heap. String type is a good example. 
    //
    // We will concentrate on the parts of String that relate to ownership.
    //
    // We've already seen string literals, where a string value is hardcorded into our
    // program. String literals are convenient, but they aren't suitable fore every
    // situation in which we may want to use text. One reason is that they're immutable.
    // Another is that not every string value can be known when we write our code:
    // for example, what if we want to take user input and store it? For these situations,
    // Rust has a second string type, String. This type manages data allocated on the heap
    // and as such is able to store an amount of text that is unknown to us at compile time.
    // You can create a String from a string literal using the from function, like so:

    let s2 = String::from("hello from String::from, allocated on the heap, right?");
    println!("{s2}");
    //* As i understand this myself at this point, this specific example is not really
    // necessary - as i know the length and the text. This could just been saved on the satck
    // using let s2 = "string".

    // The double colon :: operator allows us to namespace this particular from function 
    // under the String type rather than using some sort of name like string_from. We'll
    // discuss this syntax more in the "Method Syntax" section of Chapter 5 and when we talk
    // about namespacing with modules in "Paths for Referring to an Item in the Module Tree" in
    // Chapter 7.

    // This kind of string CAN be mutated! Important i guess!?!?
    let mut s3 = String::from("hello"); 
    s3.push_str(", world!");  // push_str() appends a literal to a String
    s3.push_str(" This got appended via .push_str() function/method!");

    println!("{s3}");

    // The big difference is that String can be mutated but literals cannot? The difference
    // is how these two types deal with memory!
}

