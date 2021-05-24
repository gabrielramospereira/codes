#include <NewPing.h>
#include <SoftwareSerial.h>  //Carrega a biblioteca SoftwareSerial

#define Emissor_Alto  8
#define Eco_Alto  9
#define Emissor_Baixo  12
#define Eco_Baixo     13
#define Dist_Max 200
#define Buzzer 2

NewPing sensorbaixo(Emissor_Baixo, Eco_Baixo, Dist_Max);
NewPing sensoralto(Emissor_Alto, Eco_Alto, Dist_Max);

SoftwareSerial mySerial(10, 11); // RX, TX - Define os pinos para a serial

int readBluetooth;

void setup() {
  
  Serial.begin(9600); //Inicia Comunicação Serial
  mySerial.begin(38400); //Inicializa a serial nas portas 10 e 11
}

void loop () {
  
  unsigned int uSbaixo = sensorbaixo.ping(); //Unsigned certifica que não receberá valores negativos e obtém tempo de Ping em microsegundos
  unsigned int uSalto = sensoralto.ping(); //Unsigned certifica que não receberá valores negativos e obtém tempo de Ping em microsegundos
  Serial.print("Distancia Sensor Baixo: ");
  int distbaixo = uSbaixo / US_ROUNDTRIP_CM; //Converte o tempo de PING em microsegundos em distância em CM  
  Serial.print(distbaixo);  
  Serial.print("CM");
  Serial.print("       Distancia Sensor Alto: ");
  int distalto = uSalto / US_ROUNDTRIP_CM; //Converte o tempo de PING em microsegundos em distância em CM
  Serial.print(distalto); 
  Serial.println("CM");
   
  mySerial.print("D");
  if(distalto <= 50){
     mySerial.print("A");
  }
  else{
     if(distbaixo<=50){
       mySerial.print("B");
     }
     else{
        mySerial.print("D");
     }
  }
  delay(2000);
  
    
  }

    
    
    
