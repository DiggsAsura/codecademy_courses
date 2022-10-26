/* while let
 * ==========
 *
 * Similar to if let, while let can make akward match sequences more tolerable. Consider the 
 * following sequence that increments i: */

fn main() {
    // Make 'optional' of type 'Option<i32>'
    let mut optional = Some(0);

    // Repeatedly try this test.
    loop {
        match optional {
            // If 'optional' destructures, evaluate the block.
            Some(i) => {
                if i > 9 {
                    println!("Greater than 9, quit!");
                    optional = None;
                } else {
                    println!("'i' is '{:?}'. Try again.", i);
                    optional = Some(i + 1);
                }
                // ^ Requires 3 indentations!
            },
            // Quite the loop when the destructure fails:
            _ => { break }
            // ^ Why should this be required? There must be at better way!
        }
    }

    /* Using while let makes this sequence much nicer:  */

    // Make 'optional' of type 'Option<i32>'
    let mut opt = Some(0);

    // This reads: "while 'let' destructures 'optional' into 'Some(i)',
    // evaluate the block ('{}'). Else 'break'.
    while let Some(i) = opt {
        if i > 9 {
            println!("Greater than 9, quit!");
            opt= None;
        } else {
            println!("'i' is '{:?}'. Try again.", i);
            opt = Some(i + 1);
        }
        // ^ Less rightward drift and doesn't require
        // explicitly handling the failing case.
    }
    // ^ 'if let' had additional optional 'else'/'else if' clauses. 
    // 'while let' does not have these.
}
