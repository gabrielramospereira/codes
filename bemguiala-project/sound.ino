int buf;
int Pinofalante = 12;
int tempo =10;
int frequencia = 0;

void setup() {
  
  Serial.begin(9600);
  pinMode(Pinofalante,OUTPUT);
  
}

void loop(){
  
  
    buf = 0;
    //Sensor Alto toca Alarme de Policia
    if (buf==0){
      for (frequencia = 1400; frequencia < 1500; frequencia += 1) {  
     tone(Pinofalante,1500,tempo);
     delay(1);  
      
    }
    delay(300);
     for (frequencia = 1400; frequencia < 1500; frequencia += 1) {  
     tone(Pinofalante,1500,tempo);
     delay(1);  
       

    }
    delay(300);
    for (frequencia = 1400; frequencia < 1500; frequencia += 1) {  
     tone(Pinofalante,1500,tempo);
     delay(1);  
    }
    }
    delay(5000);
    buf=1;
    // Definir Som para o Sensor Baixo
    if (buf==1){
     
     for (frequencia = 500; frequencia < 1500; frequencia += 1) {  
     tone(Pinofalante,1500,tempo);
     delay(1);  
      
    }
     
  }
  delay(10000);
}
