# -*- coding: cp1252 -*-
import fresh_tomatoes
import media 

#resident_evil
resident_evil=media.Movie(
    "Resident Evil",
    "The series' overarching plot focuses on multiple characters, and their roles in recurring outbreaks of zombies and other monsters, initially due to the release of the T-virus, but still more biological weapons over time, created mainly by the fictional Umbrella Corporation and various other organizations in later games.",
    "https://upload.wikimedia.org/wikipedia/commons/0/0a/The_Resident_Evil_logo.svg",
    "https://www.youtube.com/watch?v=o3ewAW0Ne94")

#the fault in or stars
the_fault_in_our_stars=media.Movie(
    "The Fault in Our Stars",
    " The story is narrated by Hazel Grace Lancaster, a 16-year-old girl with cancer. Hazel is forced by her parents to attend a support group where she subsequently meets and falls in love with 17-year-old Augustus Waters",
    "https://upload.wikimedia.org/wikipedia/en/a/a9/The_Fault_in_Our_Stars.jpg",
    "https://www.youtube.com/watch?v=9ItBvH5J6ss")

#frozen
frozen=media.Movie(
    "Frozen",
    " the film tells the story of a fearless princess who sets off on a journey alongside a rugged iceman, his loyal pet reindeer, and a naïve snowman to find her estranged sister, whose icy powers have inadvertently trapped the kingdom in eternal winter.",
    "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",
    "https://www.youtube.com/watch?v=FLzfXQSPBOg")

#twilight

twilight=media.Movie(
    "The Twilight Saga",
    "American romantic fantasy film based on the book of the same name by Stephenie Meyer. ",
    "https://upload.wikimedia.org/wikipedia/commons/d/d4/Twilight2.png",
    "https://www.youtube.com/watch?v=edLB6YWZ-R4")


#house of wax
house_of_wax=media.Movie(
    "House Of Wax",
    "American-Australian horror thriller film directed by Jaume Collet-Serra and stars Elisha Cuthbert, Chad Michael Murray, Brian Van Holt, Paris Hilton, Jared Padalecki, Jon Abrahams and Robert Ri'chard. It is based on a story by Charles Belden.",
    "https://upload.wikimedia.org/wikipedia/en/d/d9/House_Of_Wax_movie_poster.jpg",
    "https://www.youtube.com/watch?v=kbCfuFJ30t4")


movies = [resident_evil,the_fault_in_our_stars,frozen,twilight,house_of_wax]
fresh_tomatoes.open_movies_page(movies)
