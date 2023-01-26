# Using Box<T> to Point to Data on the Heap

The most straightforward smart pointer is a *box*, whose type is written **Box<T>**. Boxes allow you to
store data on the heap rather than on the stack. What remains on the stack is the pointer to the heap
data. Refer to Chapter 4 to review the difference between the stack and the heap.

Boxes don't have performance overhead, other than storing their data on the heap instea of on the
stack. But they don't have many extra capabilities either. You'll use them most often in these
situations:

    - When you have a type whose size can't be known at compile time and you want to use a value
      of that type in a context that requires an exact size
    - When you have a large amount of data and you want to transfer ownership but ensure the
      data won't be copied when you do
    - When you want to own a value and you care only that it's a type that implements a particular
      trait rather than being of a specific type

We'll demonstarte the first situation in the "Enabling Recursive Types with Boxes" section. In the
second case, transferring ownership of a large amount of data can take a long time because the data
is copied around on the stack. To improve performance in this situation, we can store the large
amount of data on the heap in a box. Then, only the small amount of pointer data is copied around
on the stack, while the data it reference stays in one place on the heap. T-he third case is known as a
*trait object* and Chapter 17 devoetes an entire section, "Using Trait Objects That Allow for Values of
Different Types", just to that topic. So what you learn here you'll apply again in Chapter 17!

