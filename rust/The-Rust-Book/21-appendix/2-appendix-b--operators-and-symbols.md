# Appendix B: Operators and Symbols

This appendix contains a glossary of Rust's syntax, includeing operators and other symbols that
appear by themselves or in the context of paths, generics, trait bounds, macros, attributes,
comments, tuples, and brackets.


## Operators

Table B-1 contains the operators in Rust, and example of how the operator would appera in context, a
short explanation, and whether that operator is overloadable. If an operator is overloadable, the
relevant trait to use to overload that operator is listed.

Table B-1: Operators

| Operator  | Example           | Explanation                   | Overloadable?     |
| --------- | ----------------- | ----------------------------- | ----------------- |
| !         | ident!(...),      |                               |                   |
|           | ident!{...},      |                               |                   |
|           | ident![...]       |                               |                   |
|
