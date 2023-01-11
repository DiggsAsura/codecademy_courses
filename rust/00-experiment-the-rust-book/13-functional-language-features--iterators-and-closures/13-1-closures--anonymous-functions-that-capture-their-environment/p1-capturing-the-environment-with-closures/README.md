# Capturing the Environment with Closures

We'll first examine how we can use closures to capture values from the environment they're defined
in for later use. Here's the scenario: Every so often, our t-shirt company gives away an exclusive,
limited-eidion shirt to someone on our mailing list as a promotion. People on the mailing list can
optionally add their favorite color to their profile. If the person hasn't specified a favorite color, they get
whatever color the company currently has the most of.

There are many ways to implement this. For example, we're going to use an enum called
**ShirtColor** that has the variants **Red** and **Blue** (limiting the number of colors available for
simplicity). We represent the company's inventory with an **Inventory** struct that has a field named
**shirts** that contains a **Vec<ShirtColor>** representing the shirt colors currently in stock. The
method **giveaway** defined on **Inventory** gets the optional shirt color preference of the free shirt
winner, and returns the shirt color the person will get. This setup is shown in Listing 13-1:

Filename: src/main.rs (see the file)
13-1: Shirt company giveaway situation

The **store** defined in **main** has two blue shirts and one red shirt remaining to distribute for this
limited-edition promotion. We call the **giveaway** method for a user with a preference for a red shirt
and a user without any preference.

Again, this code could be implemented in many ways, and here, to focus on closures, we've stuck to
concepts you've already learned except for the body of the **giveaway** method that uses a closure. In the
**giveaway** method, we get the user preference as a parameter of type **Option<ShirtColor>** and
call the **unwrap_or_else** method on **user_preference**. The unwrap_or_else method on Option<T>
is defined by the standard library. It takes one argument: a closure without any arguments that
returns a value **T** (the same type stored in the **Some** variant of the **Option<T>**, in this case
**ShirtColor**). If the **Option<T>** is the **Some** variant, **unwrap_or_else** returns the value from within
the **Some**. If the **Option<T>** is the **None** variant, **unwrap_or_else** calls the closure and returns
the value returned by the clossure.

We specify the closure expression **|| self.most_stocked()** as the argument to **unwrap_or_else**.
This is a closure that takes no parameters itself (if the closure had parameters, they would appear
between the two vertical bars). The body of the closure calls **self.most_stocked(). We're defining
the closure here ,and the implementation of **unwrap_or_else** will evaluate the closure later if the
result is needed.

Running this code prints
The user with preference Some(Red) gets Red
The user with preference None gets Blue

One interesting aspect here is that we've passed a closure that calls **self.most_stocked** on the
current **Inventory** instance. The standard library didn't need to know anything about the
**Inventory** or **ShirtColor** types we defined, or the logic we want to use in this scenario. The
closure captures an immutable reference to the **self Inventory** instance and passes it with the
code we specify to the **unwrap_or_else** method. Functions, on the other hand, are not able to
capture their environemtn this way.
