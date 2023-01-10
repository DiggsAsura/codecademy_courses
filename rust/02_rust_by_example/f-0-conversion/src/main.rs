/* Conversion
 * ===========
 *
 * Primitive types can be converted to each other through casting. (as keyword) 
 *
 * Rust addresses conversion between custom types (i.e. struct and enum) by the use of traits. The
 * generic conversion will use the From and Into traits. However there are more specific ones for
 * the more common cases, in particular when converting to and from Strings. 
 */

fn main() {
    println!("Hello, world!");
}
