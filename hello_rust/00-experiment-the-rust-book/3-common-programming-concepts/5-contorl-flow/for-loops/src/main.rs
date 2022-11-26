/* Looping Through a Collection with for
 *
 * You can choose to use the while construct to loop over elements of a collection, such as an
 * array. For example, the loop here prints every element in the array a. */

fn ex_while() {
    let a = [10, 20, 30, 40, 50];
    let mut index = 0;

    while index < 5 {       // less than
        println!("the value is: {}", a[index]);
        index += 1;
    }
}

/* Here, the code counts up through the elements in the array. It starts a index 0, and then loops
 * until it reaches the final index in the array (that is, when index < 5 is no longer true).
 * Running this code will print every element in the array. */

/* This approach is error prone; we could cause the program to panic if the index value or test
 * condidtion are incorrect. For example, if you changed the definition of the a array to have four
 * elements but forgot to update the condition to while index < 4, the code would panic. It's also
 * slow, because the compiler adds runtime code to perform the conditional check of wheter the
 * index is within the bounds of the array on every iteration through the loop.
 *
 * As a more concise alternative, use the for loop and execute some code for each item in a
 * collection:
 */

fn ex_for() {
    let a = [10, 20, 30, 40, 50];

    for element in a {
        println!("the value is: {element}");
    }
}

/* When we run this code, we'll see the same output as in with while. More importantly, we've now
 * increased the safety of the code and eliminated the chance of bugs that might result from going
 * beyond the end of the array or not going far enough and missing some items.
 *
 * Using the for loop, you wouldn't need to remember to change tany other code if you changed the
 * number of values in the array, as you would with the method used with while. 
 *
 * The safety and conciseness of for loops make them the most commonly used loop construct in Rust.
 * Even in situations in which you want to run some code a certain number of times, as in the
 * countdown example that used a while loop in the previous example (commit), most Rustaceans would
 * use a for loop. The way to do that would be to use a Range, provided by the standard library,
 * which generates all numbers in sequence starting from one number and ending before another
 * number.
 *
 * Here's what the countdown would look like using a for loop and another method we've not yet
 * talke about, rev, to reverse the range:
 *
 */

fn main() {
    for number in (1..4).rev() {
        println!("{number}!");
        std::thread::sleep_ms(1000);
    }
    println!("LIFTOFF!");

    println!("\nwhile loop example");
    ex_while();
    println!("\nfor loop example");
    ex_for();
}

