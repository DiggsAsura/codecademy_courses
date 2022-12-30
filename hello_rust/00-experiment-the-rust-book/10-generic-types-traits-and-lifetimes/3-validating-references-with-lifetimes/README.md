# Validating References with Lifetimes

Lifetimes are another kind of generic that we've already been using. Rather than ensuring that a type
has the behavior we want, lifetimes ensure that references are valid as long as we need them to be.

One detail we didn't discuss in the "Reference and Borrowing" section in Chapter 4 is that every
reference in Rust has a lifetime, which is the scope for which that reference is valid. Most of the time,
lifetimes are implicit and inferred, just like most of the time, types are inferred. We only must
annotate types when multiple types are possible. In a similar way, we must annotate lifetimes when
the lifetimes of references could be related in a few different ways. Rust requires us to annotate the
relationships using generic lifetime parameter to ensure the actual references used at runtime will
definetly be valid.

Annotating lifetimes is not even a concept most other programming languages have, so this is going
to feel unfamiliar. Alothough we won't cover lifetimes in their entirety in this chapter, we'll discuss
common ways you might encounter lifetime syntax so you can get comfortable with the concept.
