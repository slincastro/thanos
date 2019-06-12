package com.thanos.Midnight.domain;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class Message {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    private String nodeId;
    private String payload;

    public Message(String nodeId, String payload) {
        this.nodeId = nodeId;
        this.payload = payload;
    }

    public String getNodeId() {
        return nodeId;
    }

    public String getPayload() {
        return payload;
    }
}
