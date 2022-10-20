fn main() {
    ex1();
    ex2();
    ex3();
}

/* Result
 * =======
 *
 * Aside from Option<T>, the other commonly used monadic type found in the std library is
 * Result<T, E>.
 *
 * Result is a clever way of utilizing the inherent characteristics of monads to handle the
 * propagation of errors in a sensible way. 
 *
 *
 *
 * Error Handling
 * ---------------
 *
 * Result<T, E> is an enum with two variants: Ok(T) which denotes a success, and Err(E) which
 * denotes an error. */

enum Result<T, E> {
    Ok(T),
    Err(E),
}
//    let success = Ok("good job");
//    let error = Err("oops");

fn ex1() {
    // Here we have defined a function that returns Result<bool, String>.

    fn less_than_5(number: i32) -> std::result::Result<bool, String> {
        if number <= 0 {
            Err("we do not want a negative number".to_string())
        } else if number < 5 {
            Ok(true)
        } else {
            Ok(false)
        }
    }

    let answer = less_than_5(-1);

    println!("{answer:?}");

/* Thanks to the capability of monads to pass generic data on both variant arms, we can both pass a
 * successful boolean result and treat the overall successful operation of the function as its own
 * boolean result. At the same time, we are also capable of providing context for our errors.
 *
 * The fact that we can accomplish this so succinctly with a single type is wonderful. 
 *
 *
 * Error Propagation
 * ------------------
 *
 * Just the same as with Option<T>, when we need to access the inner value of a Result, we can use
 * unwrap().
 */
    
// These just wont do. 
//    let count = Ok(4);
//    println!("{}", count.unwrap());

/* This means we could utilize an if expression with the is_ok() and is_err() methods.
 *
 * let count = Ok(4);
 *
 * if count.is_ok() {
 *      println!("{}", count.unwrap());
 * }
 *
 * However, even though this is safe to do, unwrap() is discouraged because it causes our program
 * to panic. We can handle our errors in a safer manner with the if let pattern.
 * 
 *
 * let count = Ok(4);
 *
 * // Now we do not have to unwrap anything
 * if let Ok(number) = count {
 *      println!("{}", count.unwrap());
 * }
 */
}


/* The ? Operator
 * ================
 *
 * Being able to propagate errors without a lot of syntax is crucial when keeping our code clean.
 * It also gives us more time to focus on our code that works. 
 *
 * Rust has the special ? operator to accomplish precisely this.
 *
 * When we have a function that returns a Result, any expression within its body that also returns
 * a Result can be appended with ? to force any Err result to be returned immediately.
 */

fn check_counts() -> std::result::Result<bool, String> {
    fn less_than_5(number: i32) -> std::result::Result<bool, String> {
        if number <= 0 {
            Err("we do not want a negative number".to_string())
        } else if number < 5 {
            Ok(true)
        } else {
            Ok(false)
        }
    }

    let count_a = less_than_5(3)?;
    let count_b = less_than_5(2)?;
    let count_c = less_than_5(7)?;

    if count_a && count_b && count_c {
        Ok(true)
    } else {
        Ok(false)
    }
}

fn ex2() {
    let count_err = check_counts();
    println!("{count_err:?}");
}

/* In this example, if any calls to less_than_5() in our check_counts() function fail, execution of
 * code will cease, and the error value will immediately be passed as the return value of
 * check_counts(). */


/* Custom Error Types
 * -------------------
 *
 * It is common practice for crates, especially libraries, to declare their own custom error types.
 * While we can utilize any type for defining error context, enums are great candidate for errors.
 */

fn ex3() {
    // Here we are declaring a type alias for 'Result'
    type Result<T> = std::result::Result<T, ComparisonError>;

    // Represents all errors returned by this library. 
    #[derive(Debug)]
    enum ComparisonError {
        NegativeValue,
        ZeroValue,
    }

    // Thanks to our alias, now we only need to type annotate our success value

    fn less_than_5(number:i32) -> Result<bool> {
        if number < 0 { 
            Err(ComparisonError::NegativeValue)
        } else if number == 0 {
            Err(ComparisonError::ZeroValue)
        } else if number < 5 {
            Ok(true)
        } else {
            Ok(false)
        }
    }

    println!("{:?}", less_than_5(3));
}

/* To allow other error types to be carried into our own with the ? operator, we must implement
 * From<T> for the desired type.
 *
 * Here we are adding the ability to handle parsing errors from the std library:
 */

fn ex4() {
    use std::num::ParseIntError;

    enum ComparisonError {
        NegativeValue,
        ZeroValue,
        Parse(ParseIntError),
    }

    fn less_than_5(number:i32) -> std::result::Result<bool> {
        if number < 0 {
            Err(ComparisonError::NegativeValue)
        } else if number == 0 {
            Err(ComparisonError::ZeroValue)
        } else if number < 5 {
            Ok(true)
        } else {
            Ok(false)
        }
    }

    // We are passing the error from 'ParseIntError' into our own.
    impl From<ParseIntError> for ComparisonError {
        fn from(err: ParseIntError) -> ComparisonError {
            ComparisonError::Parse(err)
        }
    }

    // Now we can use the '?' operator here.
    fn less_than_5_from_str(s: &str) -> std::result::Result<bool> {
        let number = s.parse::<i32>()?;
        less_than_5(number)
    }
}
