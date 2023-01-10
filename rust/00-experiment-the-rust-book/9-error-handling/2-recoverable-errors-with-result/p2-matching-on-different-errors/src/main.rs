// Matching on Different Errors
// ============================
//
// The code in Listing 9-4 will panic! no matter why File::open failed. However, we
// want to take different actions for different failure reasons: if File::open failed
// because the file doesn't exist, we want to create the file and return the handle
// to the new file. If File::open failed for any other reason - for example, because
// we didnt't have permission to open the file-we still want the code to panic! in
// the same way it did in Listing 9-4. For this we add an inner match expression, shown
// in Listing 9-5.

use std::fs::File;
use std::io::ErrorKind; // additional errors has to be imported

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file)    => file,
        Err(error)  => match error.kind() {
            ErrorKind::NotFound => match File::create("hello.txt") {
                Ok(fc)  => fc,
                Err(e)  => panic!("Problem creating the file: {:?}", e),
            },
            other_error => {
                panic!("Problem opening the file: {:?}", other_error)
            }
        },
    };

    ex2();
}
// 9-5: Handling different kinds of errors in different ways

// The type of the value that File::open returns inside the Err variant is io::Error,
// which is a struct provided by the standard library. This struct has a method kind
// that we can call to get an io::ErrorKind value. The enum io::ErrorKind is provided
// by the standard libaray and has variants representing the different kinds of errors
// that might result from an io operation. The variant we want to use is
// ErrorKind::NotFound, which indicates the file we're trying to open doesn't exist
// yet. So we match on greeting_file_result, but we also have an inner match on
// error.kind().
//
// The condition we want to check in the inner match is wheter the value returned by
// error.kind() is the NotFound variant of the ErrorKind enum. If it is, we try to
// create the file with File::create. However, because File::create could also fial,
// we need a second arm in the inner match expression. When the file can't be created,
// a different error message is printed. The second arm of the outer match stays the
// same, so the program panics on any error besides the missing file error.
//
//
// -----------------------------------------------------------------------------
// Alternatives to Using match with Result<T, E>
// --------------------------------------------
//
// That's a lot of match! The match expression is very useful but also very much a primitive.
// In Chapter 13, you'll learn about closures, which are used with many of the methods
// defined on Result<T, E>. These methods can be more concise than using match when handling
// Result<T, E> values in your code.
//
// For example, here's another way to write the same logic as shown in Listing 9-5,
// this time using closures and the unwrap_or_else method:

fn ex2() {
    let greeting_file = File::open("hello2.txt").unwrap_or_else(|error| {
        if error.kind() == ErrorKind::NotFound {
            File::create("hello2.txt").unwrap_or_else(|error| {
                panic!("Problem creating the file: {:?}", error);
            })
        } else {
            panic!("Problem opening the file: {:?}", error);
        }
    });
}

// Although this code has the same behavior as Listing 9-5, it doesn't contain
// any match expressions and is cleaner to read. Come back to this example after
// you've read Chapter 13, and look up the unwrap_or_else method in the standard
// library documentation. Many more of these methods can clean up huge nesten match
// expressions when you're daling with errors.
// -----------------------------------------------------------------------------
