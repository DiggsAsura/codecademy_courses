/* Scoping rules
 * ==============
 *
 * Scopes play an important part in ownership, borrowing and lifetimes. That is, they indicate to
 * the compiler when borrows are valid, when resources can be freed, and when variables are created
 * or destroyed. */

fn main() {
    let scope_outer: String = String::from("Hello from the outer scope!");
    println!("{scope_outer}");
    
    {
        let scope_inner: String = String::from("Hello from the inner scope!");
        println!("{scope_inner}");
    }
}
