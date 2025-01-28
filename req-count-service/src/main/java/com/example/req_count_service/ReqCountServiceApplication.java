package com.example.req_count_service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class ReqCountServiceApplication {

	private RedisTemplate<String, String> redisTemplate;

	public ReqCountServiceApplication(RedisTemplate<String, String> redisTemplate) {
		this.redisTemplate = redisTemplate;
	}

	@GetMapping("/hello")
	public long hello() {
		String key = "request:count";
		Long count = redisTemplate.opsForValue().increment(key, 1);
		return count;
	}

	public static void main(String[] args) {
		SpringApplication.run(ReqCountServiceApplication.class, args);
	}

}
