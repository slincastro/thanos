package com.thanos.Midnight.service;

import com.thanos.Midnight.configuration.ClientConfiguration;
import org.eclipse.paho.client.mqttv3.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class Subscriber implements MqttCallback {
    
    ClientConfiguration clientConfiguration;

    MqttClient client;

    @Autowired
    public Subscriber(ClientConfiguration clientConfiguration) {
        this.clientConfiguration = clientConfiguration;
    }

    public void subscribe() {
        try {
            client = new MqttClient(clientConfiguration.getServerURI(), clientConfiguration.getClientId());
            client.connect();
            client.setCallback(this);
            client.subscribe(clientConfiguration.getTopic());

        } catch (MqttException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void connectionLost(Throwable cause) {
        // TODO Auto-generated method stub

    }

    @Override
    public void messageArrived(String topic, MqttMessage message)
            throws Exception {
        System.out.println(message);
    }

    @Override
    public void deliveryComplete(IMqttDeliveryToken token) {
        // TODO Auto-generated method stub

    }

}
