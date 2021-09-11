// C++ code


void setup()
{
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  
  pinMode(A2, INPUT);
  Serial.begin(9600);
}

void loop()
{
  int Temp = analogRead(A2);
  float volts = (Temp / 965.0) * 5;
  float c = (volts - .5) * 100;
  float f = (c * 9 / 5 + 32);
  
  if(c<=40)
  {
    digitalWrite(13, HIGH);
    digitalWrite(12, LOW);
    digitalWrite(11, LOW);
  }
  else if(c<=80)
  {
    digitalWrite(13, LOW);
    digitalWrite(11, LOW);
    digitalWrite(12, HIGH);   
  }
  else
  {
    digitalWrite(11, HIGH);
    digitalWrite(12, LOW);
    digitalWrite(13, LOW);
  }
  
  Serial.println(c);
  //Serial.println(f);
  delay(1000);
  
  
}