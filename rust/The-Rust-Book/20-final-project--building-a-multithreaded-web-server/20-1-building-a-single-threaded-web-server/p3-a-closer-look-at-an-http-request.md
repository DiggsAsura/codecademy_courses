# A Closer Look at an HTTP Request

HTTP is a text-based protocol, and a request takes this format:

```
Method Request-URI HTTP-Version CRLF
headers CRLF
message-body
```

The first line is the *request line* that holds information about what the client is requesting. The first
part of the request line indicates the *method* being used, such as **GET** or **POST**, which describes how
the client is making this request. Our client used a **GET** request, which means it is asking for
information.

The next part of the request line is /, which indicates the *Uniform Resource Identifier (URI)* the client is
requesting: a URI is almost, but not quite, the same as a *Uniform Resource Locator (URL)*. The
differece between URIs and URLs isn't important for our purposes in this chapter, but the HTTP
spec uses the term URI, so we can just mentally substitute URL for URI here.

The alst part is the HTTP version the client uses, and then the request line ends in a *CRLF sequence*.
(CRLF stands for *carriage return* and *line feed*, which are terms for the typewriter days!) The CRLF
sequence can also be written as \r\n, where \r is a carriage return and \n is a line feed. The CRLF
sequence separates the request line from the rest of the request data. Note that when the CRLF is
printed, we see a new line start rather than \r\n.

Looking at the request line data we received from running our program so far, we see thet **GET** is
the mtehod, / is the request URI, and **HTTP/1.1* is the version.

After the request line, the remaining lines tarting from **Host:** onward are headers. **GET** requests
have no body.

Try making a request from a different browser or asking froa different address, such as
*127.0.0.1:7878/test*, to see how the request data changes.

Now that we know what the browser is asking for, let's send back some data!

