#define direita 9
#define esquerda 11
void setup() {
 pinMode(direita,OUTPUT);
 pinMode(esquerda,OUTPUT);

}

void frente(){
  analogWrite(esquerda,255);
  analogWrite(direita,255);
  
  }

void parado(){
  analogWrite(esquerda,0);
  analogWrite(direita,0);
  
  }

void dir(){
  analogWrite(esquerda,255);
  analogWrite(direita,0);
  
  }


  void esq(){
  analogWrite(esquerda,0);
  analogWrite(direita,255);
  
  }

void loop() {
 frente();
 delay(2000);
 parado();
 delay(1000);
 esq();
 delay(2000);
 parado();
 delay(1000);
 dir();
 delay(2000);
 parado();
 delay(8000);
 

}
