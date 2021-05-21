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
    { "Thomas": 666 },
    { "Stian": 69420 },
    { "Margrethe": 420 },
    { "Camilla": 999 },
    { "Bottsersen": 999999999 }
]);
