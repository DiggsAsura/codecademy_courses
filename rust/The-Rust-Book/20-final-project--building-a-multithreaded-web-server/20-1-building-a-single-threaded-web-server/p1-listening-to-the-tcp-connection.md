# Listening to the TCP Connection

Our web server needs to listen to a TCP connection, so that's the first part we'll work on. The
standard library offers a **std::net** module that lsets us do this. Let's make a new project in the usual
fashion:

$ cargo new hello
    Created binay (application) 'hello' project
$ cd hello

Now enter the code in Listing 20-1 in *src/main.rs* to start. This code will listen at the local address
127.0.0.1:7878 for incoming TCP streams. When it gets an incoming stream, it will print
**Connection established!**.

*use std::net::TcpListener;

-fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();

        println!("Connection established!");
    }
}
