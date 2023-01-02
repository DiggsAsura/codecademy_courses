struct Foo<'a> {
    bar: &'a i32
}

fn baz(f: &Foo) -> &i32 {
    f.bar
}

fn main() {}

// so it wont infer the lifetimes here
