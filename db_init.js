db.createUser({
    user: 'root',
    pwd: 'toor',
    roles: [
        {
            role: 'readWrite',
            db: 'High_Scores',
        },
    ],
});
db = new Mongo().getDB("High_Scores");
db.createCollection("Scores")
db.Scores.insert([
    { "id": "Thomas", "score": 666 },
    { "id": "Stian", "score": 69420 },
    { "id": "Margrethe", "score": 420 },
    { "id": "Camilla", "score": 999 },
    { "id": "Batman", "score": 86666 }
]);
