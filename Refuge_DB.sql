create database refuge;
use refuge;

CREATE TABLE user_comments
(
commentID int primary key NOT NULL auto_increment,
commentContent varchar (500) NOT NULL,
time_stamp timestamp
);

drop table user_comments;

CREATE TABLE happy_response
(
h_respID int primary key NOT NULL auto_increment,
h_respContent varchar (300) NOT NULL
);

CREATE TABLE sad_response
(
s_respID int primary key NOT NULL auto_increment,
s_respContent varchar (300) NOT NULL
);

CREATE TABLE content_response
(
c_respID int primary key NOT NULL auto_increment,
c_respContent varchar (300) NOT NULL
);

-- Filling response tables 

INSERT INTO happy_response VALUES (01, "You are like a flower in bloom today, little one!");
INSERT INTO happy_response VALUES (02, "Excellent! Enjoy a game of Pai Sho and a calming cup of ginseng tea today.");
INSERT INTO happy_response VALUES (03, "Begin your day with something fragrant, perhaps a nice cup of jasmine tea?");
INSERT INTO happy_response VALUES (04, "Remember, perfection and power are overrated. You are wise to choose happiness and love.");

INSERT INTO sad_response VALUES (05, "I wish you luck in finding your own destiny someday. Do not let it be a destiny someone has tried to force on you. ");
INSERT INTO sad_response VALUES (06, "Sometimes life is like this dark tunnel, you can't always see the light at the end of the tunnel. But if you just keep moving, you will come to a better place.");
INSERT INTO sad_response VALUES (07, "You must never give in to despair. Allow yourself to slip down that road and you surrender to your lowest instincts. In the darkest times, hope is something you give yourself. That is the meaning of inner strength.");
INSERT INTO sad_response VALUES (08, "You sound like my nephew, always thinking you need to do things on your own, without anyone's support. There is nothing wrong with letting people who love you, help you.");

INSERT INTO content_response VALUES (09, "That's a pleasure to hear! Share some tea with a fascinating stranger today, it is one of life's true delights.");
INSERT INTO content_response VALUES (10, "I wish you more days of contentment. You are stronger and wiser and freer than you have ever been.");
INSERT INTO content_response VALUES (11, "Don't forget to hit the griddy today, little one.");
INSERT INTO content_response VALUES (12, "Sounds like a wonderful day to learn how to make some tea. Give it a try!");


-- Queries for responses : 

-- 1. Printing random response when user selects happy mood 
SELECT h_respContent 
FROM ( SELECT h_respContent FROM happy_response) 
AS combined 
ORDER BY RAND()
LIMIT 1;

-- 1. Printing random response when user selects sad mood 
SELECT s_respContent 
FROM ( SELECT s_respContent FROM sad_response) 
AS combined 
ORDER BY RAND()
LIMIT 1;

-- 1. Printing random response when user selects content mood 
SELECT c_respContent 
FROM ( SELECT c_respContent FROM content_response) 
AS combined 
ORDER BY RAND()
LIMIT 1;