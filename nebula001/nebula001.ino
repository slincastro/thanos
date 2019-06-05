#include <ESP8266WiFi.h>
#include <PubSubClient.h>

WiFiClient espClient;
PubSubClient client(espClient);
const char* mqttServer = "10.76.124.45";
const int mqttPort = 1883;

long lastMsg = 0;
char msg[50];
int value = 0;

void setup() {
  const char* ssid = "twguest";
  const char* password =  "heroic crab mammal dual swig";

  Serial.begin(115200);
  int n = WiFi.scanNetworks();
  
  for (int i = 0; i < n; i++)
  {
    Serial.println(WiFi.SSID(i));
  }

  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
  Serial.println(WiFi.status());
  delay(50);
  Serial.println("Connecting to WiFi..");
  }

  Serial.println("=================================================================");
  Serial.println(WiFi.status());
  Serial.println("Connected to the WiFi network");
  Serial.println("=================================================================");

}

void loop() {
  
  client.loop();
  
  client.setServer(mqttServer, mqttPort);
  client.connect("ESP8266Client");
  
  if (!client.connected()) {
    Serial.println("not connected...");
  }else{
    Serial.println("connected... :) ");
  }
  
  client.publish("myfirst/test", "Hola WN....");
  delay(1000);
  digitalWrite(16, LOW);
  Serial.println("Publish msg wn...");
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
    digitalWrite(BUILTIN_LED, LOW);   // Turn the LED on (Note that LOW is the voltage level
    // but actually the LED is on; this is because
    // it is acive low on the ESP-01)
  } else {
    digitalWrite(BUILTIN_LED, HIGH);  // Turn the LED off by making the voltage HIGH
  }

} 

