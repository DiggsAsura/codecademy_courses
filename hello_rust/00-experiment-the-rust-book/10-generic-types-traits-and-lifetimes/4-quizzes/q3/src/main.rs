/// Adds the string 's' to all elements of the input iterator.

fn concat_all(
    iter: impl Iterator<Item = String>,
    s: &str,
    ) -> impl Iterator<Item = String>
{
    iter.map(move |s2| s2 + s)
}

fn main() {}
