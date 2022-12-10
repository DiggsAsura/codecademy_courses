fn main() {
    let rect1 = (30, 50);

    println!(
        "The rectangle has the area: {}", area(rect1));
}

fn area(dimensions: (u32, u32)) -> u32 {
    dimensions.0 * dimensions.1
}

/* In one way, this program is better. Tuples let us add a bit of structure, and we're now passing
 * just one argument. But in another way, this version is less clear: tuples don't name their
 * elements, so we have to index into the parts of the tuple, makeing our calculation less obvious.
 *
 * Mixing up the width and height would't matter for area calculations, but if we want to draw the
 * rectangle on the screen, it would matter! We would have to keep in mind that width is the tuple
 * index 0 and height is the tuple index 1. This would be even harder to for someone else to figure
 * out and keep in mind if they were to use our code. Because we haven't conveyed the meaning of
 * our data in our code, it's now easier to indrocude errors. 
 */

