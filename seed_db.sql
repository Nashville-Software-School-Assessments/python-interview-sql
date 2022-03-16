DROP TABLE IF EXISTS State;
DROP TABLE IF EXISTS ParkType;
DROP TABLE IF EXISTS Park;


CREATE TABLE `State`(
    `state_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` INTEGER NOT NULL
);

CREATE TABLE `ParkType`(
    `park_type_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label` INTEGER NOT NULL
);

CREATE TABLE `Park`(
    `park_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `moniker` CHAR(255) NOT NULL,
    `park_type_id` INTEGER NOT NULL,
    `description` CHAR(255) NOT NULL,
    `state_id` INTEGER NOT NULL,
    FOREIGN KEY(`park_type_id`) REFERENCES `ParkType`(`park_type_id`),
    FOREIGN KEY(`state_id`) REFERENCES `State`(`state_id`)
);

INSERT INTO ParkType values (1, "National Park");
INSERT INTO ParkType values (2, "National Historic Site");
INSERT INTO ParkType values (3, "Parkway");
INSERT INTO ParkType values (4, "National Scenic Trail");

INSERT INTO State values (1, "North Carolina");
INSERT INTO State values (2, "Illinois");
INSERT INTO State values (3, "California");
INSERT INTO State values (4, "Montana");


INSERT INTO Park values (1, "Appalachian", 4, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 1);
INSERT INTO Park values (2, "Blue Ridge", 3, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 1);
INSERT INTO Park values (3, "Carl Sandburg Home", 2, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 1);
INSERT INTO Park values (4, "Great Smoky Mountains", 1, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 1);
INSERT INTO Park VALUES (5, "Lincoln Home", 2, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 2);
INSERT INTO Park VALUES (6, "Channel Islands", 3, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 3);
INSERT INTO Park VALUES (7, "Eugene O'Neill", 2, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 3);
INSERT INTO Park VALUES (8, "Yosemite", 1, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 3);
INSERT INTO Park VALUES (9, "Pony Express", 4, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 3);
INSERT INTO Park VALUES (10, "Yellowstone", 1, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 4);
INSERT INTO Park VALUES (11, "Glacier", 1, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 4);
