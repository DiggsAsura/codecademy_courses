fn main() {
    println!("Naming conventions\n");
    println!("The CamelCase convention is reserved for types and traits");

    struct UnitStruct;
//    struct TupleStruct(T); // ... with generic type T
    
    struct StructName {
//        VariantName,
    }

    type TypeAlias = u8;

    trait TraitName {}

    println!("snake_case: reserved for attributes, variables, functions and macros\n");

    // Attributes
    #![attribute_name]

    // Variables
    let variable_name = true;

    // Functions
    fn function_name() {
    //    function_call();

    }
    
    // Macros
    macro_name!();
    macro_name![];
    macro_name! {};


    println!("SCREAMING_SNAKE_CASE reserved for constants\n");
    const EIGHTY_EIGHTY: u32 = 88;




}


