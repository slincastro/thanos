
#include <DHT.h>
#include <Adafruit_Sensor.h>
 
#define DHTPIN 2

#define DHTTYPE DHT11
 

DHT dht(DHTPIN, DHTTYPE);
int greenLed = 4;
int redLed = 5;
int blueLed =3;

void setup() {
  pinMode(greenLed,OUTPUT);
  pinMode(redLed,OUTPUT);
  pinMode(blueLed,OUTPUT);
  Serial.begin(115200);
 
  dht.begin();
}


void loop() {
  blinkLed(blueLed,1000);
    // Esperamos 5 segundos entre medidas
  delay(5000);
 
  // Leemos la humedad relativa
  float h = dht.readHumidity();
  // Leemos la temperatura en grados centígrados (por defecto)
  float t = dht.readTemperature();
  // Leemos la temperatura en grados Fahrenheit
  float f = dht.readTemperature(true);
 
  // Comprobamos si ha habido algún error en la lectura
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Error obteniendo los datos del sensor DHT11");
    return;
  }
 
  // Calcular el índice de calor en Fahrenheit
  float hif = dht.computeHeatIndex(f, h);
  // Calcular el índice de calor en grados centígrados
  float hic = dht.computeHeatIndex(t, h, false);
 
  Serial.print("Humedad: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperatura: ");
  Serial.print(t);
  Serial.print(" *C ");
  Serial.print(f);
  Serial.print(" *F\t");
  Serial.print("Índice de calor: ");
  Serial.print(hic);
  Serial.print(" *C ");
  Serial.print(hif);
  Serial.println(" *F");
 
}

void blinkLed(int led,int delayTime){
  onLed(led);
  delay(delayTime);
  offLeds();
  delay(delayTime);
}

void offLeds(){
  onLed(0);
}

void onLed(int led){
  digitalWrite(greenLed,HIGH);
  digitalWrite(redLed,HIGH);
  digitalWrite(blueLed,HIGH);
  digitalWrite(led,LOW);
}

