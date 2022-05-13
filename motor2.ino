String Speed1, Speed2;
char  LorR;
int  i, s1, s2;
char DataToRead[9];
int count;
define MOTOR_A_b 11  
define MOTOR_B_a 5

void setup() {
  Serial.begin(9600);
pinMode(MOTOR_A_b, OUTPUT);
pinMode(MOTOR_B_a, OUTPUT);
}

void loop() {
  DataToRead[8] = '\n';
  Serial.readBytesUntil('\n', DataToRead, 8);
 /* For debug
  for (i = 0; i < 9; i++) {
    Serial.write(DataToRead[i]); 
    if (DataToRead[i] == '\n') break;
  }  */
  count =0; 
  Speed1= "";
  Speed2= "";
  for (i = 1; (DataToRead[i] != 'L') && (i < 9); i++) {
    Speed1 += DataToRead[i];
    count++;  }
 for(i= count+2; (DataToRead[i] !='\n') &&(i < 9); i ++){
    Speed2 += DataToRead[i]; }
    s1 = Speed1.toInt();
    s1 = 255- s1;
    s2 = Speed2.toInt();
    s2 = 255 -s2;
    // Turn right wheel 
    analogWrite(MOTOR_B_a,s1);  //모터B+의 속력을 PWM 출력
    analogWrite(MOTOR_A_b, s2);
    for(i = 0; i < 9; i++){
       DataToRead[i]  = NULL;
     }
}
