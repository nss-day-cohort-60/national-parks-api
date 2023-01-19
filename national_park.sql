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
INSERT INTO `Parks` VALUES (null, "Glacier", "A showcase of melting glaciers, alpine meadows, carved valleys, and spectacular lakes. With over 700 miles of trails, Glacier is a paradise for adventurous visitors seeking wilderness steeped in human history. Relive the days of old through historic chalets, lodges, and the famous Going-to-the-Sun Road.", "Northwest Montana", "Montana", 48.7596, 113.7870);
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

INSERT INTO `Campgrounds` VALUES (null, "Upper Pines", 5, 37, "Upper Pines is located near the Merced River in Yosemite Valley. Yosemite Valley is centrally located in the park and boasts some of Yosemite’s most iconic features. This large campground is located at 4,000 feet (1,219 m) elevation and can be accessed from all park roads. Upper Pines is within biking and walking distance of many services and trailheads in Yosemite Valley and is located on the free shuttle route. There are food and grocery services nearby at Curry Village and Yosemite Village.");

INSERT INTO `Campgrounds` VALUES (null, "Yosemite Creek", 5, 75, "Yosemite Creek Campground is located nearly 5 miles off the Tioga Road (via a rough road) 26 miles west of Tuolumne Meadows, and a little over an hour from Yosemite Valley. Located in the forest at 7,700 feet (2,300 m) many campsites are close to Yosemite Creek, which is the only water source (must be filtered, treated, or boiled). RVs and Trailers are not recommended for this harder to access, and more primitive campground. There are no visitor services close to the campground.");

INSERT INTO `Campgrounds` VALUES (null, "Black Rock", 1, 99, "This large (99 site) campground is located in the northwest corner of the park. Each campsite has a picnic table and fire ring with rest rooms and water nearby. Shopping facilities are only five miles away in the town of Yucca Valley. Campsites vary in size and can accommodate both tents and RVs. A day-use picnic area and a dump station are also available. For horse owners, a separate area is provided for camping or for staging a ride.");

INSERT INTO `Campgrounds` VALUES (null, "Indian Cove", 1, 101, "Indian Cove Campground is located off of Highway 62, thirteen miles east of Joshua Tree Village and ten miles west of Twentynine Palms on the north side of the Wonderland of Rocks. Indian Cove Road dead-ends at this secluded area. Indian Cove has 101 campsites, including thirteen group campsites. Between Memorial Day and Labor Day it is 39 reservable sites. There are vault toilets but no water at the campsites. Water is available at the small ranger station roughly two miles north of the campground.");

INSERT INTO `Campgrounds` VALUES (null, "Long Pine Key", 2, 45, "Only a few miles from the Ernest F. Coe Visitor Center, adjacent to the Long Pine Key Trail and encompassing a pleasant fishing pond, the Long Pine Key Campground provides all the essentials required for getting yourself in tune with nature.");

INSERT INTO `Campgrounds` VALUES (null, "Flamingo", 2, 15, "The campgrounds at Flamingo offer an unforgettable year-round experience in Everglades National Park.  There are plenty of pedestrian and bike trails and tons of wildlife.");

INSERT INTO `Campgrounds` VALUES (null, "Cataloochee", 3, 10, "Elevation 2,600 feet (792m) - located in historic Cataloochee Valley, is surrounded by mountain ranges and pristine streams characterized by mild winters and hot, humid summers. It offers traditional camping with the convenience of flush toilets and drinking water. There are no hookups or showers. Hammocks are allowed over the footprint of the campsite. Limited to trees 10 inches in diameter with adequate padding around the tree and only 2 hammocks may be suspended from tree.");

INSERT INTO `Campgrounds` VALUES (null, "Elkmont", 3, 23, "Elkmont Campground - elevation 2,150 feet (655m) - is the closest frontcountry camping area to Sugarlands Visitor Center in the North District of the park. The climate is characterized by mild winters and hot, humid summers. Mountain ranges and a pristine river are the backdrop for your Elkmont adventure. Elkmont Campground offers camping for both tents and RVs, with 220 sites total.");

INSERT INTO `Campgrounds` VALUES (null, "Hosmer Grove", 4, 6, "Hosmer Grove lies in the cloud belt of Haleakalā, at nearly 7,000 feet (2134m) in elevation in the Summit District. Come prepared for rain and cold weather! The forest comes to life in the early dawn with the many native birds in the area, making this a beautiful early morning hike.");

INSERT INTO `Campgrounds` VALUES (null, "Kīpahulu", 4, 20, "The Kīpahulu campground is about 1/8 mile (.2 km) south of the Kīpahulu Visitor Center. Sites overlook ocean cliffs and are a short walk from ʻOheʻo Gulch. Entry into the stream at any point in the park is prohibited. Be prepared for rain, harsh sun, and mosquitoes. There is no beach access.");

INSERT INTO `Campgrounds` VALUES (null, "Apgar", 6, 13, "Apgar campground is the largest campground in the park. It is situated in trees and provides tent and RV campers with shade and some privacy. Evening sunsets on Lake McDonald are only a short stroll, and you won't want to miss evening programs with a ranger at the Apgar Amphitheater. Many trails are located within a short drive of the campground. Five Group Sites are reservable in advance.");

INSERT INTO `Campgrounds` VALUES (null, "St Mary", 6, 32, "St. Mary Campground is the largest campground on the east side of Glacier National Park, and is conveniently located approximately a half-mile from the St. Mary Visitor Center. The visitor center offers interpretive programs, shuttle service and Red Bus tours leaving from the center. The campground sits near the entrance of the popular scenic byway, the Going-to-the-Sun Road.");

INSERT INTO `Campgrounds` VALUES (null, "Exit Glacier", 7, 10, "Exit Glacier is the primary destination for visitors to witness up close the power of the glaciers. It is also the home to the Exit Glacier Nature Center and the trail head for the Harding Icefield Trail.");

INSERT INTO `Campgrounds` VALUES (null, "Big Meadows", 8, 51, "Big Meadows Campground (mile 51.2) is centrally-located in Shenandoah National Park, providing easy access to many of the most popular destinations in the Park, including Big Meadows, Dark Hollow Falls, and Byrd Visitor Center. All sites include a place for a tent or RV, a fire ring, and a picnic table.");

INSERT INTO `Campgrounds` VALUES (null, "Lewis Mountain", 8, 26, "Lewis Mountain (mile 57.5), the smallest campground in Shenandoah National Park, appeals to those who want a little more privacy while still staying within a close distance to many of the most popular destinations in the Park, including Big Meadows (7 miles away).");

INSERT INTO `Campgrounds` VALUES (null, "Juniper Basin", 9, 3, "This campground is a strong day hike up the Tanque Verde Ridge over 6.9 miles and 3,000 feet of gain. Exceptional views can be seen throughout the hike, and habitats change quickly from desert scrub to oak savanna and pine/ juniper woodlands. Water here is very seasonal, and often dry during the spring and fall. Fires are allowed here, only from collecting dead and downed wood.");

INSERT INTO `Campgrounds` VALUES (null, "Grass Shack", 9, 11, "Grass Shack is a great campground that offers shade from large sycamores as well as other riparian species. Two of the larger streams-Chimenea Creek and Madrona Creek run through and by the campground, providing water most of the year. Fires are not allowed here being in a fragile riparian ecosystem surrounded by a thick grassland. Access is from Camino Loma Alta, and this ten mile hike climbs 2,200 feet to a campground often not affected by winter storms. Views are exceptional to the south as you climb through and above the saguaros. This is the first of two campgrounds on the Arizona Trail.");
