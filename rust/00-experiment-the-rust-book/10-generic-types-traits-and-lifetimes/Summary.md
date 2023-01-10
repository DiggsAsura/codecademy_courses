# Summary

We covered a lot in this chapter! Now that you know about generic type parameters, traits and trait bounds,
and generic lifetime parameters, you're ready to write code without repetition that works in many
different situations. Generic type parameters let you apply the code to different types. Traits
and trait bounds ensure that even though the types are generic, they'll have the behavior the code
needs. You learned how to use lifetime annoations to ensure that this flexibile code won't have any
dangling references. And all of this analysis happens at compile time, which doesn't affect runtime
performance!

Beleive it or not, there is much more to learn on the topics we discussed in this chapter: Chapter 17
discuss trait objects, which are another way to use traits. There are also more complex scenarios
involving lifetime annotations that you will only need in very advanced scenarios; for those, you
should read the Rust Referecens (link). But next, you'll learn how to write tests in Rust so you can make
sure your code is working the way it should.
