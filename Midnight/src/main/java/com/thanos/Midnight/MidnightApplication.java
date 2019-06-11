package com.thanos.Midnight;

import com.thanos.Midnight.configuration.ClientConfiguration;
import com.thanos.Midnight.service.Subscriber;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.ApplicationContext;

@SpringBootApplication
@EnableConfigurationProperties(ClientConfiguration.class)
public class MidnightApplication {

	public static void main(String[] args) {

		ApplicationContext applicationContext = SpringApplication.run(MidnightApplication.class, args);
		Subscriber service = applicationContext.getBean(Subscriber.class);
		service.subscribe();
	}

}
