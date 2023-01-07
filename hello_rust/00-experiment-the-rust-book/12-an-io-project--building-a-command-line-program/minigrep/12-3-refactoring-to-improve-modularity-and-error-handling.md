# Refactoring to Improve Modularity and Error Handling

To improve our program, we'll fix four problems that have to do with the program's structure and how
it's handling potential errors. First, our main function now performs two tasks: it parses
arguments and reads files. As our program grows, the number of separate tasks the main function
handles will increase. As function gains responsibilities, it becomes more difficult to reason about,
harder to test, and harder to change without breaking one of its parts. It's best to separate
functionality so each function is responsible for one task.

This issue also ties into the second problem: although query anf file_path are configuration
variables to our program, variables like contents are used to perform the program's logic. The
Longer main becomes, the more variables we'll need to bring into scope; the more variables we have
in scope, the harder it will be to keep track of the purpose of each. It's best to group the
configuration variables into one structure to make their purpose clear.

The third problem is that we've used expect to print an error message when reading the file fails,
but the error message just prints Should have been able to read the file. Reading a file can fail
in a number of ways: for example, the file could be missing, or we might not have permission to
open it. Right now, regardless of the situation, we'd print the same error message for everything,
which wouldn't give the user any information!

Fourth, we use expect repeatedly to handle different errors, and if the user runs our program
without specifying enough arguments, they'll get an index out of bounds error from Rust that
doesn't clearly explain the problem. It would be best if all the error-handling code were in one place
so future maintainers had only one place to consult the code if the error-handling logic needed to
change. Having all the error-handling code in one place will also ensure that we're printing messages
that will be meaningful to our end users.

Let's address these four problems by refactoring our project.


## Separation of Concerns for Binary Projects

The organizational problem of allocating responsibility for multiple tasks to the main function is
common to many binary projects. As a result, the Rust community has developed guidelines for
splitting the separate concerns of a binary program when main starts getting large. This process has
the following steps:

    - Split our program into a main.rs and lib.rs and move your program's logic to lib.rs
    - As long as your command line parsing logic is small, it can remain in main.rs
    - When the command line parsing logic starts getting complicated, extract it from main.rs and
      move it to lib.rs.

The responsibilities that remain in the main function after this process should be limited to the
following:

    - Calling the command line parsing logic with the argument values
    - Setting up any other configuration
    - Calling a run function in lib.rs
    - Handling the error if run returns an error

This pattern is about separating concerns: main.rs handles running the program, and libr.rs handles
all the logic of the task at hand. Because you can't test the main function directly, this structure lets
you test all of your program's logic by moving it into functions in lib.rs. The code that remains in
main.rs will be small enough to verify its correctness by reading it. Let's rework our program by
following this process.


