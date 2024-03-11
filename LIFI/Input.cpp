int photoPin = A0;


 int middle = 200;
  int length;
String totalString = "";
void setup() {
  Serial.begin(9600);
  Serial.println("Starting");

}

void loop() {
  if(analogRead(photoPin)>middle){
    longon();
    shortoff();
    longon();
    shortoff();
    if(analogRead(photoPin)>middle){
    longon();
    shortoff();
    length = 0;
    for(int i = 0; i < 8; i++){
      int light = analogRead(photoPin);
      if(light > middle){
        longon();
        shortoff();
        totalString += "1";
        Serial.println("1");
        length += pow(2, 6-i);
      }
      else{
        longon();
        shortoff();
        totalString += "0";
        Serial.println("0");

      }
    }
    for(int i = 0; i < length; i ++){
      int light = analogRead(photoPin);
      if(light > middle){
        longon();
        shortoff();
        totalString += "1";
        Serial.println("1");

      }
      else{
        shortoff();
        totalString += "0";
        Serial.println("0");

      }
    }
     Serial.print("Length" + length);

  }
  //int light = analogRead(photoPin);
  ///Serial.println(light);
 // delay(100);
  }
} 


void shortoff(){
      long int t1 = millis();
      while (millis() - t1 <= 200){

      }
      return;
  }

   void longon(){
      long int t1 = millis();
      while(millis() - t1 <= 2000){

      }
      return;
  }
   void longoff(){
      long int t1 = millis();
      while(millis() - t1 <= 2000){

      }
      return;
  }
