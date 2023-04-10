# Simulating a Slow Request in the Current Server Implementation

We'll look at how a slow-processing request can affect other requests made to our current server
implementation. Listing 20-10 implements handling a request to */sleep* with a simulated slow
response that will cause the server to sleep for 5 seconds before responding.

Filename: src/main.rs

```rust
use std::{
    fs,
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
    thread,
    time::Duration,
};
// --snip--

fn handle_connection(mut stream: TcpStrem) {
    // --snip--

    let (status_line, filename) = match &request_line[..] {
        "GET / HTTP/1.1" => ("HTTP/1.1 200 OK", "hello.html"),
        "GET /sleep HTTP/1.1" => {
            thread::sleep(Duration::from_secs(5));
            ("HTTP/1.1 200 OK", "hello.html")
        }
        _ => ("HTTP/1.1 404 NOT FOUND", "404.html"),
    };

    // --snip--
}
```
*Listing 20-10: Simulating a slow request by sleeping for 5 seconds*

We switched from **if** to **match** now that we have three cases. We need to explicitly match on a slice
of **request_line** to pattern match against the string literal values; **match** doesn't do automatic
referencing and dereferencing like the equality method does.

The first arm is the same as the **if** block from Listing 20-9. The second arm matches a request to
*/sleep*. When that request is received, the server will sleep for 5 seconds before rendering the
successful HTML page. The third arm is the same as the **else** block from Listing 20-9.

You can see how primitive our server is: real libraries would handle the recognition of multiple
requests in a much less verbose way!

Start the server using **cargo run**. Then open two browser windows: one for *http://127.0.0.1:7878/*
and the other for *http://127.0.0.1:7878/sleep*. If you enter the / URI a few times, as before, you'll see it
resond quickly. Buf if you enter */sleep* and then load /, you'll see that / waits until **sleep** has slept
for its full 5 seconds before loading.

There are multiple techniques we could use to avoid requests backing up behind a slow request; the
one we'll implement is a thread pool.


