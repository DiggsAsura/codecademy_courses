// Car light functions
void cRed() {
  digitalWrite(carGreen, LOW);
  digitalWrite(carYellow, LOW);
  digitalWrite(carRed, HIGH);
}
void cYellow() {
  digitalWrite(carGreen, LOW);
  digitalWrite(carRed, LOW);
  digitalWrite(carYellow, HIGH);
}
void cGreen() {
  digitalWrite(carYellow, LOW);
  digitalWrite(carRed, LOW);
  digitalWrite(carGreen, HIGH);
}

// Pedestrian light functinos
void pRed() {
  digitalWrite(pedGreen, LOW);
  digitalWrite(pedRed, HIGH);
}
void pGreen() {
  digitalWrite(pedRed, LOW);
  digitalWrite(pedGreen, HIGH);
}
