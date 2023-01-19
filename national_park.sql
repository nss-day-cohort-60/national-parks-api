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

INSERT INTO `Parks` VALUES (null, "Joshua Tree", "Two distinct desert ecosystems, the Mojave and the Colorado, come together in Joshua Tree National Park. A fascinating variety of plants and animals make their homes in a land sculpted by strong winds and occasional torrents of rain. Dark night skies, a rich cultural history, and surreal geologic features add to the wonder of this vast wilderness in southern California.", "Twentynine Palms", "California", 34.070442,-116.060294);
INSERT INTO `Parks` VALUES (null, "Everglades National Park", "Everglades National Park protects an unparalleled landscape that provides important habitat for numerous rare and endangered species like the manatee,  American crocodile, and the elusive Florida panther. An international treasure as well -  a World Heritage Site, International Biosphere Reserve, a Wetland of International Importance, and a specially protected area under the Cartagena Treaty.", "Homestead", "Florida", 25.7459, 80.5550 );
INSERT INTO `Parks` VALUES (null, "Great Smoky Mountains", "Ridge upon ridge of forest straddles the border between North Carolina and Tennessee in Great Smoky Mountains National Park. World renowned for its diversity of plant and animal life, the beauty of its ancient mountains, and the quality of its remnants of Southern Appalachian mountain culture, this is America's most visited national park.", "Gatlinburg", "Tennessee", 35.672619, -83.512053);
INSERT INTO `Parks` VALUES (null, "Haleakalā National Park", "This special place vibrates with stories of ancient and modern Hawaiian culture and protects the bond between the land and its people. The park also cares for endangered species, some of which exist nowhere else. Come visit this special place - renew your spirit amid stark volcanic landscapes and sub-tropical rain forest with an unforgettable hike through the backcountry.", "Makawao", "Hawaii", 20.7204, -156.1552);
INSERT INTO `Parks` VALUES (null, "Yosemite", "Not just a great valley, but a shrine to human foresight, the strength of granite, the power of glaciers, the persistence of life, and the tranquility of the High Sierra. First protected in 1864, Yosemite National Park is best known for its waterfalls, but within its nearly 1,200 square miles, you can find deep valleys, grand meadows, ancient giant sequoias, a vast wilderness area, and much more.", "Sierra Nevada", "California", 37.8651, 119.5383);
NSERT INTO `Parks` VALUES (null, "Glacier", "A showcase of melting glaciers, alpine meadows, carved valleys, and spectacular lakes. With over 700 miles of trails, Glacier is a paradise for adventurous visitors seeking wilderness steeped in human history. Relive the days of old through historic chalets, lodges, and the famous Going-to-the-Sun Road.", "Northwest Montana", "Montana", 48.7596, 113.7870);
INSERT INTO `Parks` VALUES (null, "Kenai Fjords National Park", "At the edge of the Kenai Peninsula lies a land where the ice age lingers. Nearly 40 glaciers flow from the Harding Icefield, Kenai Fjords' crowning feature. Wildlife thrives in icy waters and lush forests around this vast expanse of ice. Sugpiaq people relied on these resources to nurture a life entwined with the sea. Today, shrinking glaciers bear witness to the effects of our changing climate.", "Seward", "Alaska", 59.8487, -149.8163);
INSERT INTO `Parks` VALUES (null, "Shenandoah", "Shenandoah National Park is a land bursting with cascading waterfalls, spectacular vistas, fields of wildflowers, and quiet wooded hollows. With over 200,000 acres of protected lands that are haven to deer, songbirds, and black bear, there's so much to explore.", "Jollett", "Virginia", 38.4755, -78.4535);
INSERT INTO `Parks` VALUES (null, "Saguaro National Park", "Tucson, Arizona is home to the nation's largest cacti. The giant saguaro is the universal symbol of the American west. These majestic plants, found only in a small portion of the United States, are protected by Saguaro National Park, to the east and west of the modern city of Tucson. Here you have a chance to see these enormous cacti, silhouetted by the beauty of a magnificent desert sunset.", "Tuscon", "Arizona", 32.2967, 111.1666);


CREATE TABLE `Amenities` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `type` VARCHAR(255) NOT NULL
);

CREATE TABLE `Park_Amenities` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` VARCHAR(255) NOT NULL,
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
  FOREIGN KEY (`park_id`) REFERENCES `Parks` (`id`)
);
ALTER TABLE Campgrounds
ADD COLUMN description varchar(255);

CREATE TABLE `Camping_Reservations` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `start_date` DATETIME,
  `end_date` DATETIME,
  `campround_id` INTEGER NOT NULL,
  `user_id` INTEGER NOT NULL,
  FOREIGN KEY (`campround_id`) REFERENCES `Campgrounds` (`id`),
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
  `photo_id` INTEGER NOT NULL,
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
