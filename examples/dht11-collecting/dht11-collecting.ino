
#include <DHT.h> 
#define DHTPIN 2
#define DHTTYPE DHT11
 
DHT dht(DHTPIN, DHTTYPE);
int greenLed = 4;
int redLed = 5;
int blueLed =3;
bool isLogEnabled = true;

void setup() {
  pinMode(greenLed,OUTPUT);
  pinMode(redLed,OUTPUT);
  pinMode(blueLed,OUTPUT);
  Serial.begin(115200);
 
  dht.begin();
}


void loop() {
  blinkLed(blueLed,1000);
  getTemperature();   
}

String getTemperature(){
  delay(5000);
 
  float h = dht.readHumidity();
  float t = dht.readTemperature();
 
  if(isLogEnabled){
    logTemperatureServerSensor(t,h);
  }
 return "temp :"+ t + "humidity :" + h; 
}

void logTemperatureServerSensor(float temperature,float humidity){
  if (isnan(humidity) || isnan(temperature)) {
        Serial.println("Error obteniendo los datos del sensor DHT11");
        return;
    }
    
    Serial.print("Humedad: ");
    Serial.print(humidity);
    Serial.print(" %\t");
    Serial.print("Temperatura: ");
    Serial.print(temperature);
    Serial.println(" *C ");
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

