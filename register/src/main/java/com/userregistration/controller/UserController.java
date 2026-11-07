package com.userregistration.controller;

import com.userregistration.model.User;
import com.userregistration.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import jakarta.validation.Valid;

@RestController
@RequestMapping("/api")
public class UserController {
    @Autowired
    private UserService userService;

    @PostMapping("/register")
    public ResponseEntity<String> registerUser(@Valid @RequestBody User user) {
        if (userService.existsByUsername(user.getUsername())) {
            return ResponseEntity.badRequest().body("Error: Username is already taken!");
        }

        if (userService.existsByEmail(user.getEmail())) {
            return ResponseEntity.badRequest().body("Error: Email is already in use!");
        }

        userService.registerUser(user);
        return ResponseEntity.ok("User registered successfully!");
    }
}
