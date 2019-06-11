#include <DHT.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
 
#define DHTPIN 2
#define DHTTYPE DHT11

WiFiClient espClient;
PubSubClient client(espClient);

DHT dht(DHTPIN, DHTTYPE);
int greenLed = 4;
int redLed = 5;
int blueLed =3;
bool isLogEnabled = true;

const char* mqttServer = "10.76.124.45";
const int mqttPort = 1883;

long lastMsg = 0;
char msg[50];
int value = 0;

void setup() {
  pinMode(16,OUTPUT);
  pinMode(greenLed,OUTPUT);
  pinMode(redLed,OUTPUT);
  pinMode(blueLed,OUTPUT);
    
  const char* ssid = "twguest";
  const char* password =  "heroic crab mammal dual swig";

  WiFi.begin(ssid, password);
  if(isLogEnabled) {
    logWifiConnection();
  }
 
}
 
void loop() {
  
  client.loop();
  
  client.setServer(mqttServer, mqttPort);
  client.connect("ESP8266Client");

  logMqttStatus();
  String message = getTemperature();

  char charBuf[50];
  message.toCharArray(charBuf, 50);

  client.publish("myfirst/test", charBuf);
  delay(1000);
  
}

String getTemperature(){
  delay(5000);
 
  float h = dht.readHumidity();
  float t = dht.readTemperature();
 
  if(isLogEnabled){
    logTemperatureServerSensor(t,h);
  }
 return "temp :"+ String(t) + "humidity :" + String(h); 
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

void logMqttStatus(){
   if (!client.connected()) {
    Serial.println("not connected...");
    blinkLed(blueLed,1000);
  }else{
    Serial.println("connected... :) ");
    blinkLed(greenLed,1000);
  }
}

void logWifiConnection(){
  Serial.begin(115200);
  
  logWifiNetworks();
  logWifiStatus();
 
}

void logWifiStatus(){
  while (WiFi.status() != WL_CONNECTED) {
    blinkLed(redLed,1000);
    Serial.println(WiFi.status());
    delay(50);
    Serial.println("Connecting to WiFi..");
  }
  blinkLed(blueLed,1000);
  Serial.println("=================================================================");
  Serial.println(WiFi.status());
  Serial.println("Connected to the WiFi network");
  Serial.println("=================================================================");
}

void logWifiNetworks(){
  int networksNumber = WiFi.scanNetworks();
  
  for (int i = 0; i < networksNumber; i++)
  {
    Serial.println(WiFi.SSID(i));
  }  
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Switch on the LED if an 1 was received as first character
  if ((char)payload[0] == '1') {
   // digitalWrite(BUILTIN_LED, LOW);   // Turn the LED on (Note that LOW is the voltage level
    // but actually the LED is on; this is because
    // it is acive low on the ESP-01)
  } else {
    //digitalWrite(BUILTIN_LED, HIGH);  // Turn the LED off by making the voltage HIGH
  }

} 


