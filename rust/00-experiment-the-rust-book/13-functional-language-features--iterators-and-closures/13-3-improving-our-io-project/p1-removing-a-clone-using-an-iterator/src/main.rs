// Removing a clone Using an Iterator
// ==================================
//
// In Listing 12-6, we added code that took a slice of String values and created an instance of the
// Config struct by indexing into the slice and cloning the values, allowing the Config struct to
// own those values. In Listing 13-17, we've reproduced the implementation of the Config::build
// function as it was in Listing 12-23:

impl Config {
    pub fn build(args: &[String]) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let file_path = args[2].clone();

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}
// 13-17: Reproduction of the Config::build function from Listing 12-23

// At the time, we said not to worry about the inffecicient clone calls because we would remove
// them in the future. Well, that time is now!
//
// We needed clone here because we ahve a slice with String elements in the paramter args, but the
// build function doesn't own args. To return ownership of a Config instance, we had to clone the
// values from the query and filename fields of Config so the Config instance can own its values.
//
// With our new knowledge about iterators, we can change the build function to take ownership of an
// iterator as its argument instead of borrowing a slice. We'll use the iterator functionality
// instead of the code that checks the length of the slice and indexes into specific locations.
// This will clarify what the Config::build function is doing because the iterator will acccess the
// values.
//
// Once Config::build takes ownership of the iterator and stops using indexing operations that
// borrow, we can move the String values from the iterator into Config rather than calling clone
// and makeing a new allocation.
//
//
// Using the Returned Iterator Directly
// -----------------------------------
//
// Open your I/O project's src/main.rs file, which should look like this:

fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments:{err}");
        process::exit(1);
    });

    // --snip--
}

// We'll first change the start of the main function that we had in Listing 12-24 to the code in
// Listing 13-18, which this time uses an iterator. This on't compile until we update Config::build
// as well.

fn main() {
    let config = Config::build(env::args()).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    // --snip--
}
// 13-18: Passing the return value of env::args to Config::build

// The env::args function returns an iterator! Rather than collecting the iterator values into a
// vector and then passing a slice to Config::build, now we're passing ownership of the iterator
// returned from env::args to Config::build directly.
//
// Next, we need to update the definition of Config::build. In your I/O project's src/lib.rs file,
// let's change the signature of Config::build to look like Listing 13-19. This still won't compile
// because we need to update the function body.

// Filename: src/lib.rs
impl Config {
    pub fn build(args: impl Iterator<Item = String>) -> Result<Config, &'static str> {
        // --snip--
    }
}
// 13-19: Updating the signature of Config::build to expect an iterator

// The standard library documentation for the env::args function shows that the type of iterator it
// returns is std::env::Args, and that type implements the Iterator trait and returns String
// values.
//
// We've updated the signatures of the Config::build function so that parameter args has generic
// type with the trait bounds impl Iterator<Item = String> instead of &[String]. This usage of the
// impl Trait syntax we discussed in the "Traits as Parameters" section of Chapter 10 means that
// args can be any type that implements the Iterator type and returns String items.
//
// Because we're taking ownership of args and we'll be mutating args by iterating over it, we can
// add the mut keyword into the specification of the args parameter to make it mutable.
//
//
//
// Using Iterator Trait Methods Instead of Indexing
// ------------------------------------------------
//
// Next, we'll fix the body of Config::build. Because args implements the Iterator trait, we know
// we can call the next method on it! Listing 13-20 updates the code from Listing 12-23 to use the
// next method:
//
// Filename: src/lib.rs

impl Config {
    pub fn build(mut args: impl Iterator<Item = String>) -> Result<Config, &'static str> {
        args.next();

        let query = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a query string"),
        };

        let file_path = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a file path"),
        };

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}
// 13-20: Changing the body of Config::build to use iterator methods

// Remember that the first value in the return value of env::args is the name of the program. We
// want to ignore that and get to the next value, so first we call next and do nothing with the
// return value. Second, we call next to get the value we want to put in the query field of Config.
// If next returns a Some, we use a match to extract the value. If it returns None, it means not
// enough arguments were given and we return early with an Err value. We do the same thing for the
// filename value.
