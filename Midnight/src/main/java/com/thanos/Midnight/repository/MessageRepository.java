package com.thanos.Midnight.repository;

import com.thanos.Midnight.domain.Message;
import org.springframework.data.repository.CrudRepository;


public interface MessageRepository extends CrudRepository<Message, Long> {
}
