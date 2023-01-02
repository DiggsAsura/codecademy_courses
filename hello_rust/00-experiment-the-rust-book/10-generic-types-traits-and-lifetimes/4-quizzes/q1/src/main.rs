struct TestResult {
    /// Student's scores on a test
    scores: Vec<usize>,

    /// A possible value to curve all scores
    curve: Option<usize>
}

impl TestResult {
    pub fn get_curve(&self) -> &Option<usize> {
        &self.curve
    }

    /// If there is a curve, then increments all
    /// scores by the curve
    pub fn apply_curve(&mut self) {
        if let Some(curve) = self.get_curve() {
            for score in self.scores.iter_mut() {
                *score += curve;
            }
        }
    }
}

fn main() {}
