package com.userregistration;

import org.springframework.boot.SpringApplication; 
import org.springframework.context.annotation.Bean;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class UserRegistrationApplication {
    public static void main(String[] args) {
        SpringApplication.run(UserRegistrationApplication.class, args);
    }

    @Bean
    public BCryptPasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
