# Reading a File

Now we'll add functionality to read the file specified in the file_path argument. First, we need a
sample file to test it with: we'll use a file with a small amount of text over multiple lines with
some repeated words. Listing 12-3 has an Emily Dickinson poem that will work well! Create a file called
poem.txt at the root level of your project, and enter the poem "I'm Nobody! Who are you?"

(done)

With the text in place, edit src/main.rs and add code to read the file, as shown in Listing 12-4.

(done)

First, we bring in a relevant part of the standard library with a use statement: we need std::fs to
handle files.

In main, the new statement fs::read_to_string takes the file_path, opens that file, and returns
a std::io::Result<String> of the file's contents.

After that, we again add a temporary println! statement that prints the value of contents after
the flie is read, so we can check that the program is working so far.

Let's run this code with any string as the first command line argument (because we haven't
implemented the searching part yet) and the poem.txt file as the second argument:

$ cargo run -- the poem.txt
(text)


Great! The code read and then printed the contents of the file. But the code has a few flaws. At the
moment, the main function has multiple responsibilities: generally, functions are clearer and easier
to maintain if each function is responisible for only one idea. The other problem is that we're not
handling errors as well as we could. The program is still small, so these flaws aren't big problems,
but as the program grows, it will be harder to fix them cleanly. It's good practie to begin refatoring
early on when developing a program, because it's much easier to refactor smaller amounts of code.
We'll do that next.
