DROP TABLE IF EXISTS State;
DROP TABLE IF EXISTS ParkType;
DROP TABLE IF EXISTS Park;


CREATE TABLE `State`(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` INTEGER NOT NULL
);

CREATE TABLE `ParkType`(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label` INTEGER NOT NULL
);

CREATE TABLE `Park`(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` CHAR(255) NOT NULL,
    `type_id` INTEGER NOT NULL,
    `description` CHAR(255) NOT NULL,
    `state_id` INTEGER NOT NULL,
    FOREIGN KEY(`type_id`) REFERENCES `ParkType`(`id`),
    FOREIGN KEY(`state_id`) REFERENCES `State`(`id`)
);

INSERT INTO ParkType values (null, "National Park");
INSERT INTO ParkType values (null, "National Historic Site");
INSERT INTO ParkType values (null, "Parkway");
INSERT INTO ParkType values (null, "National Scenic Trail");

INSERT INTO State values (null, "North Carolina");
INSERT INTO State values (null, "Illinois");
INSERT INTO State values (null, "California");
INSERT INTO State values (null, "Montana");


INSERT INTO Park values (null, "Appalachian", 4, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 1);
INSERT INTO Park values (null, "Blue Ridge", 3, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 1);
INSERT INTO Park values (null, "Carl Sandburg Home", 2, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 1);
INSERT INTO Park values (null, "Great Smoky Mountains", 1, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 1);
INSERT INTO Park VALUES (null, "Lincoln Home", 2, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 2);
INSERT INTO Park VALUES (null, "Channel Islands", 3, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 3);
INSERT INTO Park VALUES (null, "Eugene O'Neill", 2, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 3);
INSERT INTO Park VALUES (null, "Yosemite", 1, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 3);
INSERT INTO Park VALUES (null, "Pony Express", 4, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 3);
INSERT INTO Park VALUES (null, "Yellowstone", 1, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 4);
INSERT INTO Park VALUES (null, "Glacier", 1, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 4);
