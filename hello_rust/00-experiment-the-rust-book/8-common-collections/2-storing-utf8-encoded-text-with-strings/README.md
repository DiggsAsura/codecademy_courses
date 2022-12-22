# Storing UTF-8 Encoded Text with Strings

We talked about strings in Chapter 4, but we'll look at them in more depth now. New
Rustaceans commonly get stuck on strings for a combination of three reasons: Rust's
propensity for exposing possible errors, strings being a more complicated data structure
than man programmers give them credit for, and UTF-8. These factors combine in a way that
can seem difficult when you're coming from other programming languages.

We discuss strings in the context of collections because strings are implemented as a
collection of bytes, plus some methods to proide useful functionality when those bytes
are interpreted as text. In this section, we'll talk about the operations on String that every
collection type has, such as creating, updating, and reading. We'll also discuss the way in which
String is different from other collections, namely how indexing into a String is complicated
by the differences between how people and computers interpret String data.

## What is a String?
We'll first define what we mean by the term string. Rust has only one string type
in the core language, which is the string slice str that is usually seen in its borrowed
form &str. In Chapter 4, we talked about string slices, which are references to some
UTF-8 encoded string data stored elsewhere. String literals, for example, are stored
in the program's binary and are therefor string slices.

The String type, which is provided by Rust's standard library rather than coded into
the core language, is a growable, mutable, owned, UTF-8 encoded string type. When
Rustaceans refer to "string" in Rust, they might be referring to either the String or the
slice &str types, not just one of those types. Although this section is largely about
String, both types are used heavily in Rust's standard library, and both String and
string slices are UTF-8 encoded.
