# Writing a Response

We're going to implement ssending data in response to a clinet request. Responses have the
following format:

```
HTTP-Version Status-Code Reason-Phrase CRLF
headers CRLF
message-body
```

The first line is a *status line* that contains the HTTP version used in the response, a numeric status
code that summarizes the result of the request, and a reason phrase that provides a text description
of the status code. After the CRLF sequence are any headers, another CRLF sequence, and the body
of the response.

Here is an example response that uses HTTP version 1.1, has a status code of 200, and OK reason
phrase, no headers, and no body:

```
HTTP/1.1 200 OK\r\n\r\n
```

The status code 200 is the standard success response. The text is a tiny successful HTTP response.
Let's write this to the stream as our response to a successful request! From the **handle_connection**
function, remove the **println!" that was printing the request data and replace it with the code in
Listing 20-3.

Filename: src/main.rs

```rust
fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
    let http_request: Vec<_> = buf_reader
        .lines()
        .map(|result| result.unwrap())
        .take_while(|line| !line.is_empty())
        .collect();

    let response = "HTTP:/1.1 200 OK\r\n\r\n";

    stream.write_all(response.as_bytes()).unwrap();
}
```
*Listing 20-3: Writing a tiny successful HTTP response to the stream*

The first new line defines the **response** variable that holds the success message's data. Then we call
**as_bytes** on our **response** to convert the string data to bytes. The **write_all** method on **stream**
takes a **&[u8]** and sends those bytes directly down the connection. Because the **write_all**
operation could fail, we use **unwrap** on any error result as before. Abain, in a real application you
would add error handling here.

With these changes, let's run our code and make a request. We're no longer printing any data to the
terminal, so we won't see any output other than the output from Cargo. When you load
*127.0.0.1:7878* in a web browser, you should get a blank page instead of an error. You've just hand-
codeded receiving an HTTP request and sending a response!

