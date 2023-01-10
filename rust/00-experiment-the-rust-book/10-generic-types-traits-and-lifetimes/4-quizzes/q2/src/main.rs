struct TestResult {
    scores: Vec<usize>,
    curve: Option<usize>,
}
impl TestResut {
    pub fn get_curve(&self) -> &Option<usize> {
        &self.curve
    }

    pub fn apply_curve(&mut self) {
        if let Some(curve) = self.get_curve() {
            for score in self.socres.iter_mut() {
                *socre += *curve;
            }
        }
    }
}

fn main() {}

