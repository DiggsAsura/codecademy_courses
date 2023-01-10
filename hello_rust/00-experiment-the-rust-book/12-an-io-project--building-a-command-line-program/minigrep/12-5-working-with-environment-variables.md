# Working with Environment Variables

We'll improve **minigrep** by adding an extra feature: an option for case-sensitive searching that the
user can turn on via an environment variable. We could make this feature a command line option
and require that users enter it each time they want it to apply, but by instead making it an
environment variable, we allow our users to set the environement variable once and have all their
searches be case insensitive in the terminal.



## Writing a Failing Test for the Case-Insensitive search Function

We first add a new **search_case_insensitive** function that will be called when environment
variable has a value. We'll continue to follow the TDD process, so the first step is again to write a
failing test. We'll add a new test for the new **search_case_insensitive** function and rename our old
test from **one_result* to **case_sensitive** to clarify the differences between the two tests, as shown
in Listing 12-20.

    *Filename: src/lib.rs* - check the file
    12-20: Adding a new failing test for the case-insensitive function we're about to add

Note that we've edited the old test's **contents** too. We've added a new line with the text **"Duct
tape."** using a capital D that shouldn't match the query **"duct"** when we're searching in a case-
sensitive manner. Changing the old test in this way helps ensure that we don't accidentally break the
case-sensitive search functionality that we've already implemented. This test should pass now and
should continue to pass as we work on the case-insensitive search.

The new test for the case-*insensitive* search uses "rUsT" as its query. In the
**search_case_insensitive** function we're about to add, the query **"rUsT"** should match the line
containting **"Rust:"** with a capital R and match the line **"Trust me."** even thoguh both have
different casing from the query. This is our failing test, and it will fail to compile because we haven't
yet defined the **search_case_insensitive** function. Feel free to add a skeleton implementation that
always returns an empty vector, similar to the way we did for the **search** function in Listing 12-16 to
see the test compile and fail.
