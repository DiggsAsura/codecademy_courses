# To panic! or Not to panic!

So how do you decide when you should call panic! and when you should return Result?
When code pancis, there's no way to recover. You could call panic! for any error
situation, wheter there's a possible way to recover or not, but then you're making
the decision that a situation is unrecoverable on behalf of the calling code. When
you choose to return a Result value, you give the calling code options. The calling
code could choose to attmpt to recover in a way that's appropriate for its situation,
or it could decide that an Err value in this case is unrecoverable, so it can call panic!
and turn your recoverable error into an unrecoverable  one. Therefore, returning
Result is a good default choice when you're defining a function that might fail.

In situations such as examples, prototype code, and tests, it's more appropriate to
write code that panics instead of returning a Result. Let's explore why, then discuss
situations in which the compiler can't tell that failure is impossible, but you as a human
can. The chapter will conclude with some general guidelines on how to decide wheter
to panic in library code.

## Examples, Prototype Code, and Tests

When you're writing an example to illustrate some concept, also including robust error-
handling code can make the example less clear. In examples, it's understood that a call
to a method like unwrap that could panic is meant as a placeholder for the way yo'd want
your application to handle errors, which can differ based on what the rest of your
code is doing.

Similarly, the unwrap and expect methods are very handy when prototyping, before you're
ready to decide how to handle errors. They leave clear markers in your code for when you're
ready to make your program more robust.

If a method call fails in a test, you'd want the whole test to fail, even if that method
isnt't the functionality under test. Because panic! is how a test is marked as a failure,
calling unwrap or expect is exactly what should happen.
