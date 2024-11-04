#include <ESP8266WiFi.h>

int port = 5055;
WiFiServer server(port);

const char *ssid = "Pixel_2534";
const char *password = "vlad20000";

int ENB = 14; 
int IN3 = 0; 
int IN4 = 2;  

int ENA = 16; 
int IN1 = 5; 
int IN2 = 4; 

void setup() {
  Serial.begin(9600);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid,password);

  Serial.println("connecting to wifi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    delay(500);
  }

  Serial.println("");
  Serial.print("connected to ");
  Serial.println(ssid);

  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  server.begin();

  Serial.print("open telnet and connect to IP:");
  Serial.println(WiFi.localIP());

  Serial.print(" on port ");
  Serial.println(port);

  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENB, OUTPUT);
}

void loop() {
  WiFiClient client = server.available();

  if(client) {
    if(client.connected()){
      Serial.println("client connected");
    }
  
  while(client.connected()){
      String n = client.readStringUntil('\n');//foarte impotant
      Serial.println(n);
      if (n == "stam"){
        analogWrite(ENB, 100);
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, LOW);
        analogWrite(ENA, 100);
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, LOW);
      }
      if (n == "inainte"){
        analogWrite(ENB, 255);
        digitalWrite(IN3, HIGH);
        digitalWrite(IN4, LOW);
        analogWrite(ENA, 255);
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
      }
      if (n == "inapoi"){
        analogWrite(ENB, 255);
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, HIGH);
        analogWrite(ENA, 255);
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
      }
      if (n == "dreapta"){
        analogWrite(ENB, 255);
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, LOW);
        analogWrite(ENA, 255);
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
      }
      if (n == "stanga"){
        analogWrite(ENB, 255);
        digitalWrite(IN3, HIGH);
        digitalWrite(IN4, LOW);
        analogWrite(ENA, 255);
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, LOW);
      }
      if (n == "inainte si stanga"){
        analogWrite(ENB, 255);
        digitalWrite(IN3, HIGH);
        digitalWrite(IN4, LOW);
        analogWrite(ENA, 100);
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
      }
      if (n == "inainte si dreapta"){
        analogWrite(ENB, 100);
        digitalWrite(IN3, HIGH);
        digitalWrite(IN4, LOW);
        analogWrite(ENA, 255);
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
      }
      if (n == "inapoi si stanga"){
        analogWrite(ENB, 255);
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, HIGH);
        analogWrite(ENA, 100);
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
      }
      if (n == "inapoi si dreapta"){
        analogWrite(ENB, 100);
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, HIGH);
        analogWrite(ENA, 255);
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
      }

      client.flush();
    }
    client.stop();
    Serial.println("");
    Serial.println("client disconnected");
  }  
}