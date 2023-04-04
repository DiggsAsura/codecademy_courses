use hello_macro::HelloMacro;
use hello_macro_derive::HelloMacro;

#[derive(HelloMacro)]
struct GDI;

fn main() {
    GDI::hello_macro();
}
