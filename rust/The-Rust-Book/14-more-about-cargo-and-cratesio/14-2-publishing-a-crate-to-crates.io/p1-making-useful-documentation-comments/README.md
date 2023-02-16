# Making Useful Documentation Comments

Accurately documenting your packages will help other users know how and when to use them, so it's
worth investing the time to write documentation. In Chapter 3, we discussed how to comment Rust
code using two slashes, //. Rust also has a particular kind of comment for documentation, known
conveniently as a *documentation comment*, that will generate HTML documentation. The HTML
displays the contents of documentation comments for public API items intened for programmers
interested in knowing how to *use* your crate as opposed to how your crate is *implemented*.

Documentation comments use three slashes, ///, instead of two and support Markdown notation
for formatting the text. Place documentation comments just before the item they're documenting.
Listing 14-1 shows documentation comments for an **add_one** function in a crate named **my_crate**.

Filename: src/lib.rs
(please check it)

Listing 14-1: A documentation comment for a function


Here, we give a description of what the **add_one** function does, start a section with the heading
**Examples**, and then provide code that demonstrates how to use the **add_one** function. We can
generate the HTML documentation from this documentation comment by running **cargo doc**. This
command runs the **rustdoc** tool distributed with Rust and puts the generated HTML
documentation in the *target/doc* directory.

For convenience, running **cargo doc --open** will build the HTML for your current crate's
documentation (as well as the documentation for all of your crate's dependencies) and open the
result in a web browser. Navigate to the **add_one** function and you'll see how the text in the
documentation comments is rendered, as shown in Figure 14-1.



