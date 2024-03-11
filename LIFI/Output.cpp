void setup() {
  // put your setup code here, to run once:
    pinMode(13, OUTPUT);

	Serial.begin(9600);

  //20 miiseconds
long int t1 = millis();
      digitalWrite(13, LOW); 
     
     //so that we get to wait a lil
      while (millis() - t1 <= 2000){

      }

  String payload = "10100000011010";

  int totlength = payload.length();
  int restlength = 0; 
  for(int i = 1; i < 8; i ++){
    if(payload.substring(i, i+1).equals("1")){
      restlength += pow(2, 7-i);
    }
  }

	Serial.println(restlength);
  for(int i = 0; i < restlength+8; i ++){
      if(payload.substring(i, 1+ i).equals("1")){
          longon();
      }
      else{
          longoff();
      }
      shortoff();
  }

}

void loop() {
  // put your main code here, to run repeatedly:

}
void shortoff(){
      long int t1 = millis();
      digitalWrite(13, LOW); 
      while (millis() - t1 <= 200){

      }
      return;
  }

   void longon(){
      long int t1 = millis();
      digitalWrite(13, HIGH); 
      while(millis() - t1 <= 2000){

      }
      digitalWrite(13, LOW); 
      return;
  }
   void longoff(){
      long int t1 = millis();
      digitalWrite(13, LOW); 
      while(millis() - t1 <= 2000){

      }
      return;
  }
