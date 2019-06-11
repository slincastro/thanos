package com.thanos.Midnight.configuration;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;

@Configuration
@ConfigurationProperties(prefix="spring.app.mqtt-client")
public class ClientConfiguration {

    private String serverURI;
    private String clientId;
    private String topic;

    public String getServerURI() {
        return serverURI;
    }

    public String getClientId() {
        return clientId;
    }

    public String getTopic() {
        return topic;
    }

    public void setServerURI(String serverURI) {
        this.serverURI = serverURI;
    }

    public void setClientId(String clientId) {
        this.clientId = clientId;
    }

    public void setTopic(String topic) {
        this.topic = topic;
    }
}
