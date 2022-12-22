fn main() {
  let mut v = vec![1, 2, 3];
  let mut v2 = Vec::new();
  for i in &mut v {
    v2.push(i);
  }
  *v2[0] = 5;
  let a = *v2[0];
  let b = v[0];
  println!("{a} {b}");

  println!("{:?}", v);
  // why is v[0] now 5?

}
