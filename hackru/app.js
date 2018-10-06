var fs = require('fs');
var express = require('express');
var bodyParser = require('body-parser');
var pg = require('pg');


var app = express();
// Use static files 
app.use(express.static(__dirname));
app.use(bodyParser.json());
var urlencodedParser = bodyParser.urlencoded({ extended: true });

app.set('view engine', 'ejs');
app.use(express.static(__dirname));

// Get form data using get-from-data module 

app.get('/', function(req, res){
    res.sendFile(__dirname+ '/index.html');
});

app.post('/', urlencodedParser, function(req, res){
    var userInput = req.body.userInput;
    console.log(userInput);

    var conString = "postgres://erhjbmgq:JjwVb_0QxvpAOIMVUVDicYfDUHtZAmt6@stampy.db.elephantsql.com:5432/erhjbmgq";
    var client = new pg.Client(conString);
    var name = "Amish";
    client.connect(function(err){
        if (err){
            return console.error("Could not connect to postgres", err);
        }
        console.log("Connected to the SQL databade");
        client.query("INSERT INTO InputUserSentiment(Name, Sentiment) VALUES($1, $2)", [name, userInput]);

        // client.query(sql, function (err, result) {
        //     if (err) throw err;
        //     console.log("1 record inserted");
        //   });
   });
});

app.listen(3000);
console.log("App Listening to port 3000");