/**
	Title: gonzalez-aggregateQueries.js
    Author: Janis Gonzalez
    Date: 04/23/23
    Description: Aggregate queries for assignment 6.2
 */

// query to show a list of documents in the houses collection
db.houses.find()
    // query to show a list of documents in the student’s collection
db.students.find()
    // query to add a document to the student’s collection.  
db.students.insertOne({ firstName: "Janis", lastName: "Gonzalez", studentId: "s1019", houseId: "h1009" })
    // query to prove the document was added to the user’s collection
db.students.find({ firstName: "Janis" })
    // query to delete the document created in step  
db.students.deleteOne({ firstName: "Janis" })
    // query to prove the document was deleted to the user’s collection
db.students.find({ firstName: "Janis" })

// query to show a list of students by house 
db.houses.aggregate([{ $lookup: { from: "students", localField: "houseId", foreignField: "houseId", as: "inhabitants" } }])

// query to show a list of students for the eagle mascot
db.houses.aggregate([{ $match: { mascot: 'Eagle' } }, { $lookup: { from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'Ravenclaw', } }])

// query to show a list of students for house gryffindor 
db.houses.aggregate([{ $lookup: { from: "students", pipeline: [{ $match: { houseId: "h1007" } }], as: "GryffindorInhabitants" } }])