/** 
    Title: gonzalez-mongodbShell.js
    Author: Janis Gonzalez
    Date: 4/09/2023
    Description: Queries for Assignment 4.2 MongoDB Shell 
 */

// displays all documents in user's collection
db.users.find()

// searches users with an email that matches the input (jbach@me.com)
db.users.find({ "email": "jbach@me.com" })

// searches users with the last name that matches the input (Mozart)
db.users.find({ "lastName": "Mozart" })

// searches users with the first name that matches the input (Richard)
db.users.find({ "firstName": "Richard" })

// searches users with the employeeId that matches the input (1010)
db.users.find({ "employeeId": "1010" })