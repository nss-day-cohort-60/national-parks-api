CREATE TABLE `Users` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `first_name` VARCHAR(255) NOT NULL NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL
);

CREATE TABLE `Parks` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `history` VARCHAR(255) NOT NULL,
  `city` VARCHAR(255) NOT NULL,
  `state` VARCHAR(255) NOT NULL,
  `longitude` FLOAT NOT NULL,
  `latitude` FLOAT NOT NULL
);

CREATE TABLE `Amenities` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `type` VARCHAR(255) NOT NULL
);

CREATE TABLE `Park_Amenities` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` VARCHAR(255),
  `amenity_id` INTEGER NOT NULL,
  `park_id` INTEGER NOT NULL,
  FOREIGN KEY (`amenity_id`) REFERENCES `Amenities` (`id`),
  FOREIGN KEY (`park_id`) REFERENCES `Parks` (`id`)
);

CREATE TABLE `Wildlife` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `information` VARCHAR(255) NOT NULL,
  `wildlife_group_id` INTEGER NOT NULL,
  FOREIGN KEY (`wildlife_group_id`) REFERENCES `Wildlife_Groups` (`id`)
);

CREATE TABLE `Wildlife_Groups` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `name` VARCHAR(255) NOT NULL
);

CREATE TABLE `Park_Wildlife` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `park_id` INTEGER NOT NULL,
  `wildlife_id` INTEGER NOT NULL,
  FOREIGN KEY (`park_id`) REFERENCES `Parks` (`id`),
  FOREIGN KEY (`wildlife_id`) REFERENCES `Wildlife` (`id`)
);

CREATE TABLE `Natural_Attractions` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `name` VARCHAR(255) NOT NULL
);

CREATE TABLE `Park_Natural_Attractions` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `park_id` INTEGER NOT NULL,
  `attraction_id` INTEGER NOT NULL,
  FOREIGN KEY (`park_id`) REFERENCES `Parks` (`id`),
  FOREIGN KEY (`attraction_id`) REFERENCES `Natural_Attractions` (`id`)
);

CREATE TABLE `Campgrounds` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `park_id` INTEGER NOT NULL,
  `available_sites` INTEGER NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  FOREIGN KEY (`park_id`) REFERENCES `Parks` (`id`)
);

CREATE TABLE `Camping_Reservations` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `start_date` DATETIME,
  `end_date` DATETIME,
  `campground_id` INTEGER NOT NULL,
  `user_id` INTEGER NOT NULL,
  FOREIGN KEY (`campground_id`) REFERENCES `Campgrounds` (`id`),
  FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`)
);

CREATE TABLE `Events` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `start_date` DATETIME,
  `park_id` INTEGER NOT NULL,
  FOREIGN KEY (`park_id`) REFERENCES `Parks` (`id`)
);

CREATE TABLE `Event_Registration` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `event_id` INTEGER NOT NULL,
  `user_id` INTEGER NOT NULL,
  FOREIGN KEY (`event_id`) REFERENCES `Events` (`id`),
  FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`)
);

CREATE TABLE `Blogs` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `post_body` VARCHAR(255) NOT NULL,
  `date_created` DATETIME,
  `user_id` INTEGER NOT NULL,
  `park_id` INTEGER NOT NULL,
  `photo_url` INTEGER,
  FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`),
  FOREIGN KEY (`park_id`) REFERENCES `Parks` (`id`)
);

CREATE TABLE `Favorite_Types` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `type` VARCHAR(255) NOT NULL
);

CREATE TABLE `User_Favorites` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `type_id` INTEGER NOT NULL,
  `post_id` INTEGER NOT NULL,
  `user_id` INTEGER NOT NULL,
  FOREIGN KEY (`type_id`) REFERENCES `Favorite_Types` (`id`),
  FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`),
  FOREIGN KEY (`post_id`) REFERENCES `Blogs` (`id`),
  FOREIGN KEY (`post_id`) REFERENCES `Event_Registration` (`id`)
);

CREATE TABLE `Photos` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `url` VARCHAR(255) NOT NULL,
  `user_id` INTEGER NOT NULL,
  `park_id` INTEGER NOT NULL,
  FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`),
  FOREIGN KEY (`park_id`) REFERENCES `Parks` (`id`)
);

CREATE TABLE `Blog_Photos` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `blog_id` INTEGER NOT NULL,
  `photo_id` INTEGER NOT NULL,
  FOREIGN KEY (`blog_id`) REFERENCES `Blogs` (`id`),
  FOREIGN KEY (`photo_id`) REFERENCES `Photos` (`id`)
);

