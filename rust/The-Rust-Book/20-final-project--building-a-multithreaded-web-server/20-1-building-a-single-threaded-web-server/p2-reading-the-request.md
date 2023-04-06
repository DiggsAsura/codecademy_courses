# Reading the Request

Let's implement the functionality to read the request from the browser! To separate the concerns of
first getting a connection and then taking some action with the connection, we'll start a new function
for processing connections. In this new **handle_connection** function, we'll read data from the TCP
stream and print it so we can see the data being sent from the browser. Chane the code to look like
Listing 20-2.

Filename: src/main.rs
```rust
use std::{
    io::{predule::*, BufReader},
    net::{TcpListener, TcpStream},
};

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();

        handle_connection(stream);
    }
}

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
    let http_request: Vec<_> = buf_reader
        .lines()
        .map(|result| result.unwrap())
        .take_while(|line| !line.is_empty())
        .collect();

    println!("Request: {:#?}", http_request);
}
```
*Listing 20-2: Reading from the **TcpStream** and printing the data*


