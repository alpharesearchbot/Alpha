#include <Wire.h>
 float RateRoll, RatePitch, RateYaw;
 float RateCalibrationRoll, RateCalibrationPitch,RateCalibrationYaw;
 int RateCalibrationNumber;
 void gyro_signals(void) {
    Wire.beginTransmission(0x68);

   // Enter the are off low pass fillter
   // low pass filler momery address 0x1A 
    Wire.write(0x1A);  // low pass fillter to becaues motor vibration will case some rution 
    Wire.write(0x05); // low pass fillter range 1 -7 
    Wire.endTransmission();

  // sencivity for the scall factor 
    Wire.beginTransmission(0x68);
    Wire.write(0x1B);
    Wire.write(0x8);
    Wire.endTransmission();

   /// measure the gyro signal 
    Wire.beginTransmission(0x68);
    Wire.write(0x43);
    Wire.endTransmission();
    Wire.requestFrom(0x68,6);
 int16_t GyroX=Wire.read()<<8 | Wire.read();
 int16_t GyroY=Wire.read()<<8 | Wire.read();
 int16_t GyroZ=Wire.read()<<8 | Wire.read();
 RateRoll=(float)GyroX/65.5;
 RatePitch=(float)GyroY/65.5;
 RateYaw=(float)GyroZ/65.5;
 }
 void setup() {
    Serial.begin(57600);
    pinMode(13, OUTPUT);
    digitalWrite(13, HIGH);
    // Set the I2C clock to 400kHz
    Wire.setClock(400000);
    Wire.begin();
    delay(250);
    // activate the gyro
    Wire.beginTransmission(0x68);
    Wire.write(0x6B);
    Wire.write(0x00);
    Wire.endTransmission();
    for (RateCalibrationNumber=0;
         RateCalibrationNumber<2000;
          RateCalibrationNumber ++) {
              gyro_signals();
              RateCalibrationRoll+=RateRoll;
              RateCalibrationPitch+=RatePitch;
              RateCalibrationYaw+=RateYaw;
              delay(1);
    }
 RateCalibrationRoll/=2000;
 RateCalibrationPitch/=2000;
 RateCalibrationYaw/=2000;
 }
 void loop() {
 gyro_signals();
 RateRoll-=RateCalibrationRoll;
 RatePitch-=RateCalibrationPitch;
 RateYaw-=RateCalibrationYaw;
 Serial.print("Roll rate [°/s]= ");
 Serial.print(RateRoll);
 Serial.print(" Pitch Rate [°/s]= ");
 Serial.print(RatePitch);
 Serial.print(" Yaw Rate [°/s]= ");
 Serial.println(RateYaw);
 delay(50);
 }