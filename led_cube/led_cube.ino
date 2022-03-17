/*
    LED 3*3*3 CUBE

    Version  : 01
    Author   : Kapthura Jayasanka
    Date     : 2015.04.09

    Blog     : http://kapthura.blogspot.com/p/home-page.html
    Google+  : https://plus.google.com/+KapthuraJayasanka/posts
    LinkedIn : https://lk.linkedin.com/pub/kapthura-jayasanka/6b/444/b94
*/

int ledpin; //Use for Pattern 5
int dt=0; //Use for Pattern 1 Delay time


void setup() {
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
}


void loop() {
  clearn();
  p1C();
  clearn();
  p2C();
  clearn();
  p3C();
  clearn();
  p4C();
  clearn();
  p5C1();
  clearn();
  p6C();
}


//Active & deactive Levels
//Level 1
void L1A(){
  digitalWrite(13, HIGH);
}

void L1DA(){
  digitalWrite(13, LOW);
}

//Level 2
void L2A(){
  digitalWrite(12, HIGH);
}

void L2DA(){
  digitalWrite(12, LOW);
}

//Level 3
void L3A(){
  digitalWrite(11, HIGH);
}

void L3DA(){
  digitalWrite(11, LOW);
}

//Tren off all Levels & all Led's
void clearn(){
  L1DA();
  L2DA();
  L3DA();
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10,LOW);
}

/*Pattern 1
Runner*/

void p1(int dt){
for (int i = 2; i <=10; i++){
   digitalWrite(i, HIGH);
  delay(dt);
  digitalWrite(i, LOW);
  delay(dt);
  }
}

/*Pattern 1
Controller*/
void p1C(){
  L1A();
  p1(200);
  L1DA();

  L2A();
  p1(200);
  L2DA();

  L3A();
  p1(200);
  L3DA();
}


//**********************************


/*Pattern 2
Runner */

void p2(){
  int dt2=100;
  digitalWrite(6, HIGH);
  delay(dt2);
  digitalWrite(6, LOW);
  delay(dt2);
  digitalWrite(7, HIGH);
  delay(dt2);
  digitalWrite(7, LOW);
  delay(dt2);
  digitalWrite(10, HIGH);
  delay(dt2);
  digitalWrite(10, LOW);
  delay(dt2);
  digitalWrite(9, HIGH);
  delay(dt2);
  digitalWrite(9, LOW);
  delay(dt2);
   digitalWrite(8, HIGH);
  delay(dt2);
  digitalWrite(8, LOW);
  delay(dt2);
  digitalWrite(5, HIGH);
  delay(dt2);
  digitalWrite(5, LOW);
  delay(dt2);
  digitalWrite(2, HIGH);
  delay(dt2);
  digitalWrite(2, LOW);
  delay(dt2);
  digitalWrite(3, HIGH);
  delay(dt2);
  digitalWrite(3, LOW);
  delay(dt2);
  digitalWrite(4, HIGH);
  delay(dt2);
  digitalWrite(4, LOW);
  delay(dt2);
}

/*Pattern 2
Controller*/
void p2C(){

  L1A();
  p2();
  L1DA();

  L2A();
  p2();
  L2DA();

  L3A();
  p2();
  L3DA();

}


//*******************************


/*Pattern 3
Runner*/

void p3(){
  digitalWrite(2, HIGH);
  digitalWrite(3, HIGH);
  digitalWrite(4, HIGH);
  digitalWrite(5, HIGH);
  digitalWrite(6, HIGH);
  digitalWrite(7, HIGH);
  digitalWrite(8, HIGH);
  digitalWrite(9, HIGH);
  digitalWrite(10, HIGH);
  delay(300);
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10,LOW);
  delay(300);
}


/*Pattern 3
Controller*/
void p3C(){
  L1A();
  p3();
  L1DA();
  L2A();
  p3();
  L2DA();
  L3A();
  p3();
  L3DA();
  L3A();
  p3();
  L3DA();
  L2A();
  p3();
  L2DA();
  L1A();
  p3();
  L1DA();
}


//*******************************


/*Pattern 4
Runner */
void p4(){
  digitalWrite(2, HIGH);
  digitalWrite(3, HIGH);
  digitalWrite(4, HIGH);
  digitalWrite(5, HIGH);
  digitalWrite(6, HIGH);
  digitalWrite(7, HIGH);
  digitalWrite(8, HIGH);
  digitalWrite(9, HIGH);
  digitalWrite(10, HIGH);
}

/*Pattern 4
Controller*/
void p4C(){
  L1A();
  L2A();
  L3A();
  p4();
  delay(1000);
}


//*******************************


/*Pattern 5 (Have two runners 5a,5b)
Runner 5a*/
void p5a(int ledpin){
  int dt3=150;
clearn();
  L1A();
  digitalWrite(ledpin, HIGH);
  delay(dt3);
  digitalWrite(ledpin, LOW);
  delay(dt3);
  L1DA();
  L2A();
  digitalWrite(ledpin, HIGH);
  delay(dt3);
  digitalWrite(ledpin, LOW);
  delay(dt3);
  L2DA();
  L3A();
  digitalWrite(ledpin, HIGH);
  delay(dt3);
  digitalWrite(ledpin, LOW);
  delay(dt3);
  L3DA();
}

/*Pattern 5b
Runner*/
void p5b(int ledpin){
  int dt3=80;
  clearn();
  L3A();
  digitalWrite(ledpin, HIGH);
  delay(dt3);
  digitalWrite(ledpin, LOW);
  delay(dt3);
  L3DA();
  L2A();
  digitalWrite(ledpin, HIGH);
  delay(dt3);
  digitalWrite(ledpin, LOW);
  delay(dt3);
  L2DA();
  L1A();
  digitalWrite(ledpin, HIGH);
  delay(dt3);
  digitalWrite(ledpin, LOW);
  delay(dt3);
  L1DA();
}

/*Pattern 5
Controller*/
void p5C1(){
  p5b(2);
  p5b(3);
  p5b(4);
  p5b(7);
  p5b(10);
  p5b(9);
  p5b(8);
  p5b(5);
}


//*************************

/*Pattern 6
Runner*/
void p6(){
  int dt4=350;
  digitalWrite(2, HIGH);
  digitalWrite(4, HIGH);
  digitalWrite(6, HIGH);
  digitalWrite(8, HIGH);
  digitalWrite(10, HIGH);
  delay(dt4);
  digitalWrite(2, LOW);
  digitalWrite(4, LOW);
  digitalWrite(6, LOW);
  digitalWrite(8, LOW);
  digitalWrite(10, LOW);
  delay(dt4);
}


/*Pattern 6
Controller*/
void p6C(){
  L1A();
  p6();
  L1DA();
  L2A();
  p6();
  L2DA();
  L3A();
  p6();
  L3DA();
}
