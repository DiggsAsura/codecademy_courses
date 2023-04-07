# Validating the Request and Selectively Responding

Right now, our web server will return the HTML in the file no matter what the client requested. Let's
add functionality to check that the browser is requesting / before returning the HTML file and return
an error if the browser request anything else. For this we need to modify **handle_connection**, as
shown in Listing 20-6. This new code checks the content of the request received against what we
know a request for / looks like and adds **if** and **else** blocks to treat requests differently.

Filename: src/main.rs
```rust
// --snip--

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
    let request_line = buf_reader.lines().next().unwrap().unwrap();

    if request_line == "GET / HTTP/1.1" {
        let status_line = "HTTP/1.1 200 OK";
        let contents = fs::read_to_string("hello.html").unwrap();
        let length = contents.len();

        let response = format!(
            "{status_line}\r\nContent-Length: {length}\r\n\r\n{contents}"
        );

        stream.write_all(response.as_bytes()).unwrap();
    } else {
        // some other request
    }
}
```
*Listing 20-6: Handling requests to / differently from other requests*

We're only going to be looking at the first line of the HTTP request, so rather than reading the entire
request into a vector, we're calling **next** to get the first item from the iterator. The first **unwrap**
takes care of the **Option** and stops the program if the iterator has no items. The second **unwrap**
handles the **Result** and has the same effect as the **unwrap** that was in the **map** added in Listing 20-
2.

Next, we check the **request_line** to see if it equals the request line of a GET request to the / path. If
it does, the **if**block returns contents of our HTML file.

If the **request_line** does *not* equal the GET request to the / path, it means we've received some
other request. We'll add code to the **else** block in a moment to respond to all other requests.

Run this code now and request *127.0.0.1:7878*; you should get the HTML in *hello.html*. If you make
any other request, such as *127.0.0.1:7878/something-else*, you'll get a connection error like those you
saw when running the code in Listing 20-1 and Listing 20-2.

Now let's add the code in Listing 20-7 to the **else** block to return a response with the status code
404, which signals that the content for the request was not found. We'll also return some HTML for a
page to render in the browser indicating the response to the end user.

Filename: src/main.rs
```rust
// --snip--
} else {
    let status_line = "HTTP/1.1 404 NOT FOUND";
    let contents = fs::read_to_string("404.html").unwrap();
    let length = contents.len();

    let response = format!(
        "{status_line}\r\nContent-Length: {length}\r\n\r\n{contents}"
    };

    stream.write_all(response.as_bytes()).unwrap();
}
```
*Listing 20-7: Responding with status code 404 and an error page if anything other than / was requested*

Here, our response has a status line with status code 404 and the reason phrase **NOT FOUND**. The
body of the response will be the HTML in the file *404.html*. You'll need to create a *404.html* file next to
*hello.html* for the error page; again feel free to use any HTML you want or use the example HTML in
Listing 20-8.

Filename: 404.html
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Hello!</title>
    </head>
    <body>
        <h1>Ooops!</h1>
        <p>Sorry, I don't know what you're asking for.</p>
    </body>
</html>
```
*Listing 20-8: Sample content for the page to send back with any 404 response*

With these changes, run your server again. Requesting *127.0.0.1:7878* should return the contents of
*hello.html*, and any other request, like *127.0.0.1:7878/foo*, should return the error HTML from
*404.html*.


