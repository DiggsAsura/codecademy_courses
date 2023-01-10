# Hashing Functions

By default, HashMap uses a hashing function called SipHash that can provide resistance
to Denial of Services (DoS) attacks involving hash tables*. This is not the fastest
hashing algorithm available, but the trade-off for better security that comes with the
drop of performce is worth it. If you profile your code and find that the default hash
function is too slow for your purposes, you can swith to another function by specifying
a different hasher. A hasher is a type that implements the BuildHasher trait. We'll
talk about traits and how to implement them in Chapter 10. You don't necessarily
have to implement your own hasher from scratch; crates.io has libraries shared
by other Rust users that proivde hasher implementing many common hashing algorithms.

https://en.wikipedia.org/wiki/SipHash
