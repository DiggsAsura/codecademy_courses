/* Other Slices
 *
 * String slices, as you might imagine, are specific to strings. But there's a more general slice
 * type, too. Consider this array: 
 *
let a = [1, 2, 3, 4, 5];
*
* Just as we might want to refer to a part of a string, we might want to refer to part of an array.
* We'd do so like this:
*
let a = [1, 2, 3, 4, 5];
let slice = &a[1..3];
assert_eq!(slice, &[2, 3]);
*
* This slice has the type &[i32]. It works the same way as string slices do, by storing a reference
* to the first element and a length. You'll use this kind of slice for all sorts of other
* collections. We'll discuss these collections in detail when we talk about vectors in Chapter 8.
*/

fn main() {
    let a = [1, 2, 3, 4, 5];

    let slice = &a[1..3];  // 3 inclusive. Output 2 3
    assert_eq!(slice, &[2, 3]);

    println!("{slice:?}");
}
