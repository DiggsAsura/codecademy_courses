// Lifetime Annotations in Method Definitions
// ==================================================
//
// When we implement methods on struct with lifetimes, we use the same syntax as that of generic
// type parameters shown in Listing 10-11. Where we declare and use the lifetime parameters depends
// on wheter they're related to the struct fields or the method parameters and return values.
//
// Lifetime names for struct fields always need to be declared after the impl keyword and then used
// after the struct's name, because those lifetimes are part of the struct's type.
//
// In method signatures inside the impl block, references might be tied to the lifetime of
// references in the struct's fields, or they might be independent. In addition, the lifetimes
// elision rules often make it so that lifetime annotations aren't necessary in method signtuares.
// Let's look at some examples using the struct named ImportnatExcerpt that we defined in Listing
// 10-24.
//
// First, we'll use a method named level whose only parameter is a reference self and whose return
// value is an i32, which is not reference to anything:
impl<'a> ImportantExcerpt<'a> {
    fn level(&self) -> i32 {
        3
    }
}

// The lifetime parameter declaration after impl and its use after the type name are required, but
// we're not required to annotate the lifetime of the reference to self because of the first
// elision rule.
//
// Here is an example where the third lifetime elision rule applies:
imp<'a> ImportantExcerpt<'a> {
    fn announce_and_return_part(&self, announcement: &str) -> &str {
        println!("Attention please: {}", announcement);
        self.part
    }
}

// There are two input lifetimes, so Rust applies the first lifetime elision rule and gives both
// &self and annoucement their own lifetimes. Then, because one of the parameters is &self, the
// return type gets the lifetime of &self, and all lifetimes have been accounted for.
//
