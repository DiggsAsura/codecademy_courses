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

    // Original code
    /*
    pub fn apply_curve(&mut self) {
        if let Some(curve) = self.get_curve() {
            for score in self.scores.iter_mut() {
                *score += curve;
            }
        }
    } */

    // fix one
    // Nope, immutable borrow
    /*
    pub fn apply_curve(&mut self) {
        if let Some(curve) = self.get_curve().as_ref() {
            for score in self.scores.iter_mut() {
                *score += curve;
            }
        }
    } */

    // fix two
    // Nope
    /*
    pub fn apply_curve(&mut self) {
        if let Some(curve) = self.get_curve() {
            for score in self.scores.iter() {
                *score += *curve;
            }
        }
    }*/

    // fix three
    // works!
    /*
    pub fn apply_curve(&mut self) {
        if let Some(curve) = self.curve {
            for score in self.scores.iter_mut() {
                *score += curve;
            }
        }
    } */

    // fix four
    // works as well, but i think this is the worst option, because of clone.
    pub fn apply_curve(&mut self) {
        if let Some(curve) = self.get_curve() {
            for score in self.scores.clone().iter_mut() {
                *score += *curve;
            }
        }
    }
}

fn main() {}
