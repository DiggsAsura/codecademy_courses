# Shared-State Concurrency

Message passing is a fine way of handling concurrency, but it's not the only one. Another method
would be for multiple threads to access the same shared data. Consider this part of the slogan from
the Go language documentation again: "do not communicate by sharing memory".

What would communicating by sharing memory look like? In addition, why would message-passing
enthusiasts caution not to use memory sharing?

In a way, channels in any programming language are similar to single ownership, because once you
transfer a value down a channel, you sjhould no longer use that value. Shared memory concurrency
is like mulitple ownership: multiple threads can access the same memory location at the same time.
As you saw in Chapter 15, where smart pointers made multiple ownership possible, multiple
ownership can add complexity because these different owners need managing. Rust's type system and
ownership rules greatly assist in getting this management correct. For example, let's look at
mutexes, one of the more common concurrency primitives for shared memory.
