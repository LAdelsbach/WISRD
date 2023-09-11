#include <Grove_LED_Bar.h>



 #include <Servo.h>

Servo pointer; 
Servo middle; 
Servo ring; 
Servo pinky; 


void setup() {
  pointer.attach(2);
  middle.attach(3);
  ring.attach(4);
  pinky.attach(5);

  //5 4 0 2
 rock();
  delay(500);
  paper();
  delay(500);

  scissors();


  delay(500);
  rock();
}

void loop() {
}

void rock(){
  pointer.write(0);
  middle.write(0);
  ring.write(0);
  pinky.write(0);  
}
void paper(){
  pointer.write(150);
  middle.write(150);
  ring.write(150);
  pinky.write(150);  
}

void scissors(){
  pointer.write(150);
  middle.write(150);
  ring.write(0);
  pinky.write(0);  
}


// Grove - EMG Sensor demo code
// This demo will need a Grove - Led Bar to show the motion
// Grove - EMG Sensor connect to A0
// Grove - LED Bar connect to D8, D9
// note: it'll take about serval seconds to detect static analog value
// when you should hold your muscle static. You will see led bar from level 10 turn to
// level 0, it means static analog value get ok









// Grove_LED_Bar bar(9, 8,0, LED_BAR_10);

// int max_analog_dta = 300;   // max analog data
// int min_analog_dta = 100;   // min analog data
// int static_analog_dta = 0;  // static analog data


// // get analog value
// int getAnalog(int pin) {
//   long sum = 0;

//   for (int i = 0; i < 32; i++) {
//     sum += analogRead(pin);
//   }

//   int dta = sum >> 5;

//   max_analog_dta = dta > max_analog_dta ? dta : max_analog_dta;  // if max data
//   min_analog_dta = min_analog_dta > dta ? dta : min_analog_dta;  // if min data

//   return sum >> 5;
// }

// void setup() {
//   Serial.begin(115200);

//   long sum = 0;

//   for (int i = 0; i <= 10; i++) {
//     for (int j = 0; j < 100; j++) {
//       sum += getAnalog(A0);
//       delay(1);
//     }

//     bar.setLevel(10 - i);
//   }

//   sum /= 1100;

//   static_analog_dta = sum;

//   Serial.print("static_analog_dta = ");
//   Serial.println(static_analog_dta);
// }

// int level = 5;
// int level_buf = 5;

// void loop() {

//   int val = getAnalog(A0);  // get Analog value

//   int level2;

//   if (val > static_analog_dta)  // larger than static_analog_dta
//   {
//     level2 = 5 + map(val, static_analog_dta, max_analog_dta, 0, 5);
//   } else {
//     level2 = 5 - map(val, min_analog_dta, static_analog_dta, 0, 5);
//   }

//   // to smooth the change of led bar
//   if (level2 > level) {
//     level++;
//   } else if (level2 < level) {
//     level--;
//   }

//   if (level != level_buf) {
//     level_buf = level;
//     bar.setLevel(level);
//   }

//   delay(10);
// }












// #include <Grove_LED_Bar.h>

// //BE SURE USE CORRESPONDING DEVICE
// //Grove_LED_Bar bar(6, 7, 0, LED_CIRCULAR_24);
// //FOR LED_BAR_10
// Grove_LED_Bar bar(7, 6, 0, LED_BAR_10); // Clock pin, Data pin, Orientation

// void setup() {
//     // nothing to initialize
//     bar.begin();
// }

// void loop() {
//     // Turn on all LEDs
//     bar.setBits(0x3ff);
//     delay(1000);

//     // Turn off all LEDs
//     bar.setBits(0x0);
//     delay(1000);

//     // Turn on LED 1
//     // 0b000000000000001 can also be written as 0x1:
//     bar.setBits(0b000000000000001);
//     delay(1000);

//     // Turn on LEDs 1 and 3
//     // 0b000000000000101 can also be written as 0x5:
//     bar.setBits(0b000000000000101);
//     delay(1000);

//     // Turn on LEDs 1, 3, 5, 7, 9
//     bar.setBits(0x155);
//     delay(1000);

//     // Turn on LEDs 2, 4, 6, 8, 10
//     bar.setBits(0x2AA);
//     delay(1000);

//     // Turn on LEDs 1, 2, 3, 4, 5
//     // 0b000000000011111 == 0x1F
//     bar.setBits(0b000000000011111);
//     delay(1000);

//     // Turn on LEDs 6, 7, 8, 9, 10
//     // 0b000001111100000 == 0x3E0
//     bar.setBits(0b000001111100000);
//     delay(1000);

//     /*******************Only used for LED_CIRCULAR_24******/
//     // Turn on LEDs 11, 12, 13, 14, 15, 16, 17
//     bar.setBits(0b000000011111110000000000);
//     delay(1000);

//     // Turn on LEDs 18, 19, 20, 21, 22, 23, 24
//     bar.setBits(0b111111100000000000000000);
//     delay(1000);
//     /******************************************************/
// }