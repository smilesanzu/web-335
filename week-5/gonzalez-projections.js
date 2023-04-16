/**
	Title: gonzalez-projections.js
    Author: Janis Gonzalez
    Date: 04/16/2023
    Description: users collection queries
 */

// query to add a new user to the user’s collection
db.users.insertOne({ firstName: 'Giuseppe', lastName: 'Verdi', employeeId: '444', email: 'verdi@me.com', dateCreated: new Date });
// query to update Mozart’s email address to mozart@me.com
db.users.update({ email: "wmozart@me.com" }, { $set: { email: "mozart@me.com" } })
    // query to prove the email address was updated
db.users.find({ email: 'mozart@me.com' })
    // query to list all documents in the user’s collection and with projections to only display the firstName, lastName, and email 
db.users.find({}, { firstName: 1, lastName: 1, email: 1 })