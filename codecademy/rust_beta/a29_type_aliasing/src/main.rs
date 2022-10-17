fn main() {
    ex1();
    ex2();
}

/* 
 * Type Aliasing
 * ==============
 *
 * Readable code is paramount to collaboration and maintainable software. This short article is
 * meant to introduce the idea that well-named code can sometimes be the best form of
 * documentation.
 *
 *
 * Type Aliasing
 * ---------------
 *
 * Being able to define a custom, named type is beneficial in separating out concepts within our
 * code. But sometimes an existing datatype fits our requirements without us needing to define any
 * additional functionality. 
 *
 * In these situations, we can provide an alternative name for the type using the type keyword.
 * This is referred to as Type Alias. 
 */

fn ex1() {
    // Here we are creating the associated type 'Name' which resolves to Rust's 'String' type
    type Name = String;

    // This is equivalent to 'Person(String)'
    struct Person(Name);

    fn print_name(person: Person) {
        let name = person.0;
        println!("{}", name);
    }

    /* This does nothing to the original type; aliasing is only a tool to help the programmer
     * better define the codebase. */
}


/* Import Aliasing
 * ----------------
 *
 * We can provide alternate names for imports by utilizing the 'as' keyword. This helps to avoid
 * naming conflicts as well as allows us to make our type names concise. 
 *
 * Here we will imagine we are using an external crate called dataplace which has an unfortunate
 * internal type named String. 
 */

fn ex2() {
    /*use dataplace::value::String as DbString;
    use std::collections::BTreeMap as Tree;

    fn db_values(values: Vec<(DbString, DbString)>) -> Tree<String, String> 
    {
        let mut tree = Tree::new();
        for (k, v) in values {
            tree.insert(k.into(), v.into());
        }
        tree
    } */
    println!("this function is fictional");
}


