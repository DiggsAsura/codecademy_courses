/* Enum Values
 *
 * We can create instances of each of the two variants of IpAddrKind like this:
 *
 * let four = IpAddrKind::V4;
 * let six  = IpAddrKind::V6;
 *
 * Note that the variants of the enum are namespaced under its identifier, and we use a double
 * colon to separate the two. This is useful because now both values IpAddrKind::V4 and
 * IpAddrKind::V6 are of the same type: IpAddrKind. We can then, for instance, define a function
 * that takes any IpAddrKind:
 *
 * fn route(ip_kind: IpAddrKind) {}
 *
 * And we can call this function with either variant:
 *
 * rout(ipAddrKind::V4);
 * route(IpAddrKind::V6);
 *
 * Using enums has even more advantages. Thinking more about our IP address type, at the moment we
 * don't have a way to store the actual IP address data; we only know what kind it is. Given that
 * you just learned about structs in Chapter 5, you might get tempted to tackle this problem with
 * structs as shown here: */

enum IpAddrKind {
    V4,
    V6,
}

struct IpAddr {
    kind: IpAddrKind,
    address: String,
}

fn main() {
    let home = IpAddr {
        kind: IpAddrKind::V4,
        address: String::from("127.0.0.1"),
    };

    let loopback = IpAddr {
        kind: IpAddrKind::V6,
        address: String::from("::1"),
    };
    
    // ex2
    ex2();
    ex7();
}

/* Here, we've defined a struct IpAddr that has two fields: a kind field that is of type IpAddrKind
 * (the enum we defined previously) and an address field of type String. We have two instances of
 * the struct. The first is home, and it has the value of IpAddrKind::V4 as its kind with
 * associated address data of 127.0.0.1. The second instance is loopback. It has the other variant
 * of IpAddrKind as its kind value, V6, and has address ::1 associated with it. We've used a struct
 * to bundle the kind and address values together, so now the variant is associated with the value. 
 *
 * However, representing the same concept using just an enum is more concise: rather than an enum
 * inside a struct, we can put data directly into each enum variant. This new definition of the
 * IpAddr enum says that both V4 and V6 variants will have associated String values: */

fn ex2() {
    #[derive(Debug)]
    enum IpAddr {
        V4(String),
        V6(String),
    }

    let home = IpAddr::V4(String::from("127.0.0.1"));
    let loopback = IpAddr::V6(String::from("::1"));

    println!("home: {:?}", home);
    println!("loopback: {:?}", loopback);
}

/* We attach data to each variant of the enum directly, so there's no need for an extra struct.
 * Here it's also easier to see another detail of how enums work: the name of each enum variant
 * that we define also becomes a function that constructs an instance of the enum. That is,
 * IpAddr::V4() is a function call that takes a String argument and returns an instance of the
 * IpAddr type. We automatically get this constructor function defined as a result of defining the
 * enum.
 *
 * There's another advantage of using an enum rather than a struct: each variant can have different
 * types and amounts of associated data. Version four type IP addresses will always have four
 * numeric components that will have values between 0 and 255. If we wanted to store V4 addresses
 * as four u8 values but still express V6 addresses as one String value, we wouldn't be able to
 * with a struct. Enums handle this case with ease: */

fn ex3() {
    enum IpAddr {
        V4(u8, u8, u8, u8),
        V6(String),
    }
    
    let home = IpAddr::V4(127, 0, 0, 1);
    let loopback = IpAddr::V6(String::from("::1"));
}

/* We've shown several different ways to define data structures to store version four and version
 * six IP addresses. However, as it turns out, wanting to store IP addresses and encode which kind
 * they are is so common that the standard library has a definition we can use! Let's look at how
 * the standard library defines IpAddr: it has the exact enum and variants that we've defined and
 * used, but it embeds the address data inside the variants in the form of two different structs,
 * which are defined differently for each variant.*/

fn ex4() {
    struct Ipv4Addr {
        // --snip--
    }

    struct Ipv6Addr {
        // --snip--
    }

    enum IpAddr {
        V4(Ipv4Addr),
        V6(Ipv6Addr),
    }
}

/* This code illustrates that you can put any kind of data inside an enum variant: strings, numeric
 * types, or structs, for example. You can even include another enum! Also, standard librarty types
 * often not much more complicated than what you might come up with.
 *
 * Note that even though the standard libaray contains a definition of IpAddr, we can still create
 * and use our own definition without conflict because we haven't brought the standard library's
 * definition into our scope. We'll talk more aobut bringing types into scope in Chapter 7. 
 *
 * Let's look at another example of an enum here. This one has a wide variety of types embedded in
 * its variants. */

fn ex5() {
    enum Message {
        Quit,
        Move { x: i32, y: i32 },
        Write(String),
        ChangeColor(i32, i32, i32),
    }
}

/* The enum has four variants with different types: 
 * - Quit has no data associated with it at all.
 * - Move has named fields like a struct does. 
 * - Write has a single String.
 * - ChangeColor has three i32 values.
 *
 * Defining an enum with variants such as the ones here is similar to defining different kinds of
 * struct definitions, except the enum doesn't use the struct keyword and all the variants are
 * grouped together under the Message type. The following structs could hold the same data that the
 * preceding enum variants hold: */

fn ex6() {
    struct QuitMessage; // unit struct
    struct MoveMessage {
        x: i32,
        y: i32,
    }
    struct WriteMessage(String); // tuple struct
    struct ChangeColorMessage(i32, i32, i32); // tuple struct
}

/* But if we used the different structs, which each have their ownt type, we couldn't as easily
 * define a function to take any of these kinds of messages as we could with the Message enum
 * defined in the previous example, which is a single type. 
 *
 * There is one more similarity between enums and structs: just as we're able to define methods on
 * structs using impl, we're also able to define methods on enums. Here's a method named call that
 * we could dfeine on our Message enum: */

fn ex7() {
    #[derive(Debug)]
    enum Message {
        Quit,
        Move { x: i32, y: i32 },
        Write(String),
        ChangeColor(i32, i32, i32),
    }

    impl Message {
        fn call(&self) {
            println!("call");
        }
    }
    
    let m = Message::Write(String::from("hello"));
    m.call();
    println!("m: {:?}", m);
}

/* The body of the method would use self to get the value that we called the method on. In this
 * example, we've created a variable m that has the value Message::Write(String::from("hello")),
 * and that is what self will be in the body of the call method when m.call() runs.
 *
 * Let's look at another enum in the standard library that is very common and useful: Option. */
