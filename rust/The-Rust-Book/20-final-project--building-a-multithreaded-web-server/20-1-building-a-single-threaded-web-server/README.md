# Building a Single-Threaded Web Server

We'll start by getting a single-threaded web server working. Before we begin, let's look at a quick
overview of the protocols involved in building web servers. The details of these protocols are beyond
the scope of this book, but a brief overview will give you the information you need.

The two main protocols involved in web servers are *Hyptertext Transfer Protocol (HTTP)* and
*Transmission Control Protocol (TCP)*. Both protocols are *request-response* protocols, meaning a *client*
initiates requests and a *server* listens to the request and provides a response to the client. The
contents of those requests and responses are defined by the protocols.

TCP is the lower-level protocol that describes the details of how information gets from one server to
another but doesn't specify what that information is. HTTP builds on top of TCP by defining the
contents of the requests and responses. It's technically possible to use HTTP with other protocols,
but in the vast majority of cases, HTTP sends its data over TCP. We'll work with the raw bytes of TCP
and HTTP requests and responses.


