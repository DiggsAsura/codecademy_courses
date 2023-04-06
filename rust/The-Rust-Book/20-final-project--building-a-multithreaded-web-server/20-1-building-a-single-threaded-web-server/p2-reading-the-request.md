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

We bring **std::io__prelude** and **std::io::BufReader** into scope to get access to traits and types
that let us read from and write to the stream. In the **for** loop in the **main** function, insstead of
printing a message that says we made a connection, we now call the new **handle_connection**
function and pass the **stream** to it.

In the **handle_connection** function, we create a new **BufReader** instance that wraps a mutable
reference to the **stream. BufReader** adds buffering by managing calls to the **std::io::Read** trait
methods for us.

We create a variable named **http_request** to collect the lines of the request the browser sends to
our server. We indicate that we want to collect these lines in a vector by adding the **Vec<_>** type
annotation.

**BufReader** implements the **std::io::BufRead** trait, which provides the **lines** method. The **lines**
method returns an iterator for **Result<String, std::io::Error>** by splitting the stream of data
whenever it sees a newline byte. To get each **String**, we map and **unwrap** each **Result**. The
**Result** might be an error in the data isn't valid UTF-8 or if there was a problem reading from the
stream. Again, a production program should handle these errors more gracefully, but we're
choosing to stop the program in the error case for simplicity.

The browser signals the end of an HTTP request by sending two newline characters in a row, so to
get one request from the stream, we take lines until we get a line that is the empty string. Once
we've collected the lines into the vector, we're printing them out usng pretty debug formatting so we
can take a look at the instructions the web browser is sending to our server.

Let's try this code! Start the program and make a request in a web browser again. Note that we'll still
get an error page in the browser, but our program's output in the terminal will now look similar to
this:

```
$ cargo run
   Compiling hello v0.1.0 (file:///projects/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 0.42s
     Running `target/debug/hello`
Request: [
    "GET / HTTP/1.1",
    "Host: 127.0.0.1:7878",
    "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language: en-US,en;q=0.5",
    "Accept-Encoding: gzip, deflate, br",
    "DNT: 1",
    "Connection: keep-alive",
    "Upgrade-Insecure-Requests: 1",
    "Sec-Fetch-Dest: document",
    "Sec-Fetch-Mode: navigate",
    "Sec-Fetch-Site: none",
    "Sec-Fetch-User: ?1",
    "Cache-Control: max-age=0",
]
```

Depending on your browser, you might get slightly different output. Now that we're printing the
request data, we can see why we get multiple connections from one browser request by looking at
the path after **GET** in the first line of the request. If the repeated connections are all requesting /, we
know the browser is trying to fetch / repeatedly because it's not getting a response from our
program.

Let's break down this request data to understand what the browser is asking of our program.
