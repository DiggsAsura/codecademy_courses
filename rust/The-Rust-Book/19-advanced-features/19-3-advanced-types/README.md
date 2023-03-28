# Advanced Types

The Rust type system has some features that we've so far mentioned but havent't yet discussed. We'll
start by discussing newtypes in general as we examine why newtypes are useful as types. Then we'll
move on to type aliases, a feature similar to newtypes but with slightly different semantics. We'll also
discuss the ! type and dynamically sized types.


## Using the Newtype Pattern for Type Safety and Abstraction

The newtype pattern is also useful for tasks beyond those we've discussed so far, including statically
enforcing that values are never confused and indicating the units of a value. You saw an example of
using newtypes to indicate units in Listing 19-15: recall that the **Millimeter** and **Meters** structs
wrapped **u32** values in a newtype. If we wrote a function with a parameter of type **Millimeters**, we
couldn't compile a program that accidentally tried to call that function with a value of type **Meters**
or a plain **u32**.

We can also use the newtype pattern to abstract away some implementation details of a type: the
new type can expose a public API that is different from the API of the private inner type.

Newtypes can also hide internal implementation. F-or example, we could provide a **People** type to
wrap a **HashMap<i32, String>** that stores a person's ID associated with their name. Code using
**People** would only interact with the public API we provide, such as a method to add a name string
to the **People** collection; that code woudn't need to know that we assign an **i32** ID to names
internally. The newtype pattern is a lightweight way to achieve encapsulation to hide
implementation details, which we discussed in the "Encapsulation that Hides Implementation
Details" section of Chapter 17.
