Why R? 2019 hackathon
================

This repository hosts data and scripts for Data Visualizations Hackathon ![](http://whyr.pl/foundation/images/fulls/whyr2019/hackathon/plakat_hackathon2.jpg)

-   [Event Details](#event-details)
-   [The challenge](#the-challenge)
-   [Data](#data)
-   [Fishnet of Warsaw (WGS84)](#fishnet-of-warsaw-wgs84)
-   [Hackathon data](#hackathon-data)
-   [Scripts](#scripts)

> Idea based on [m-wrzr/populartimes](https://github.com/m-wrzr/populartimes)

Event Details
=============

-   Website: [whyr.pl/2019/hackathon](http://whyr.pl/2019/hackathon)
-   Place: Faculty of Economic Sciences, University of Warsaw
-   Address: Długa 44/50, Warsaw
-   Date: 26.09.2019
-   Start - open doors: 8:30
-   Presentations: 17:00 - 18:00
-   End - closing remarks: 18:00
-   **For?** For everyone interested in data visualizations and data presentation!
-   **Tech?** No tech skills are needed to participate in the event!

The challenge
=============

Let’s find out which areas citizens of Warsaw visit most frequently! In this hackathon, we will track the behaviour of people based on the GCP data.

[Google Cloud Platform](https://cloud.google.com/) (GCP) enables 6 APIs that provide information about maps, traffic, routes or places around the globe. We decided to use GCP APIs to prepare a data set of places in Warsaw with the information about its type, address and geographical localization; where rating, number or reviews and occupancy (popular times per day) were taken from Google Search Engine!

Having such an interesting data one can immediately think about potential use cases!

-   What is the best place to make a new advertisement in the city?
-   What are the blank spaces on the map where a specific service is missing?
-   Are the most crowded places properly equipped with a sufficient amount of city bike stations? What are the - moving/traffic trends throughout the day?
-   Does the occupancy of the areas correspond to the real estate prices?

**Imagine other use cases you can invent, the moment you link the data with other sources.**

Data
====

Fishnet of Warsaw (WGS84)
-------------------------

![](https://raw.githubusercontent.com/WhyR2019/hackathon/master/plots/warsaw_05_wgs84.png)

To call [GCP Places API](https://developers.google.com/places/web-service/details) we used a fishnet of Warsaw in WSG84 system. The fishnet we generated present grid of Warsaw after every 500 metres. For each point we called [GCP Places API](https://developers.google.com/places/web-service/details) to get all places of a specific [type]((https://developers.google.com/places/web-service/supported_types#table1)) within a range of `floor(500*sqrt(2)/2)` (~353) metres. Based on all 2058 points, we were able to extract all available places of a specific type in Warsaw.

Since [GCP Places API](https://developers.google.com/places/web-service/details) is a paid platform, on a limit allowed for NGOs for free, we were able just to download few types of places. Below you can find types that we are planning to extract, displayed in the order of priority

-   restaurants
-   local\_government\_office
-   supermarket
-   movie\_theater
-   gas\_station
-   gym
-   post\_office
-   cafe
-   night\_club
-   pharmacy
-   city\_hall
-   police
-   dentist
-   doctor
-   school
-   furniture\_store
-   hospital
-   veterinary\_care

Hackathon data
--------------

> Full data will be annouanced a day before the event.

You can find the example data to understand the structure of collected information in the [data/](https://github.com/WhyR2019/hackathon/tree/master/data) directory. Before we annouance the full data, you can find there

-   amrit.csv
    -   example based on 7 Amrit Oriental Foods restaurants around Warsaw
    -   [GCP Places API](https://developers.google.com/places/web-service/details) allows to extract
        -   place\_id (GCP realted id of the place)
        -   name (place name)
        -   user\_ratings\_total (number of ratings)
        -   rating (the average rating)
        -   types ([types of places](https://developers.google.com/places/web-service/supported_types#table1) the place is assigned to)
        -   price\_level (the level of prices)
            -   0 — Free
            -   1 — Inexpensive
            -   2 — Moderate
            -   3 — Expensive
            -   4 — Very Expensive
        -   vicinity (a simplified address for the place)
        -   lat (latitude of the place in WGS84 *system*)
        -   lng (longitude of the place in WGS84 *system*)

| name                | vicinity                           | place\_id                    | types                                             |  rating|  user\_ratings\_total|  price\_level|       lat|       lng|
|:--------------------|:-----------------------------------|:-----------------------------|:--------------------------------------------------|-------:|---------------------:|-------------:|---------:|---------:|
| Amrit Oriental Food | Grochowska 207, Warszawa           | ChIJHSD5vb\_NHkcRI6Yvq0Hqqto | restaurant,food,point\_of\_interest,establishment |     3.7|                   631|             1|  52.24431|  21.08623|
| Amrit Oriental Food | Warecka 8, Warszawa                | ChIJ1ezHy1bNHkcRIEaHR0Xh9oU  | restaurant,food,point\_of\_interest,establishment |     3.8|                   333|             2|  52.23652|  21.01618|
| Amrit Oriental Food | Ludwika Kondratowicza 25, Warszawa | ChIJr0MAO7HOHkcRXuv9xy42ap8  | restaurant,food,point\_of\_interest,establishment |     3.9|                  2176|             1|  52.29346|  21.03412|
| Amrit Oriental Food | Grójecka 20C, Warszawa             | ChIJK6TJl5fMHkcRLkBTQJV7yJM  | restaurant,food,point\_of\_interest,establishment |     4.0|                  2292|             1|  52.22200|  20.98575|
| Amrit Oriental Food | aleja "Solidarności" 117, Warszawa | ChIJp1tSmn3MHkcRRJzzo3s7cz8  | restaurant,food,point\_of\_interest,establishment |     4.0|                  1617|             1|  52.24175|  20.99436|
| Amrit Oriental Food | Adama Mickiewicza 27, Warszawa     | ChIJnbAmX\_LLHkcRpQZrQm8glMg | restaurant,food,point\_of\_interest,establishment |     4.0|                  2126|             1|  52.26832|  20.98578|

-   amrit\_popular\_times.csv
    -   example based on 7 Amrit Oriental Foods restaurants around Warsaw
    -   Google Search allows to extract
        -   the day of week
        -   the hour of the day
        -   the occupancy index 
            - the index denotes how busy a particular location is on a scale of 1-100 
            (1 being the least busy, 100 being the busiest the location gets, 
            0 --- the location is closed).
            Values are based on a combination of Google searches, Google maps app location data, and local traffic data.
        -   the occupancy text
        -   av\_time\_spent (average time spent in the place)
        -   place\_id, name and vicinity to join with [GCP Places API](https://developers.google.com/places/web-service/details) data

|  hour|  occupancy\_index| occupancy\_text  | day    | av\_time\_spent                    | place\_id                    | name                | vicinity                 |
|-----:|-----------------:|:-----------------|:-------|:-----------------------------------|:-----------------------------|:--------------------|:-------------------------|
|     6|                 0| NA               | Sunday | People typically spend 30 min here | ChIJHSD5vb\_NHkcRI6Yvq0Hqqto | Amrit Oriental Food | Grochowska 207, Warszawa |
|     7|                 0| NA               | Sunday | People typically spend 30 min here | ChIJHSD5vb\_NHkcRI6Yvq0Hqqto | Amrit Oriental Food | Grochowska 207, Warszawa |
|     8|                 0| NA               | Sunday | People typically spend 30 min here | ChIJHSD5vb\_NHkcRI6Yvq0Hqqto | Amrit Oriental Food | Grochowska 207, Warszawa |
|     9|                 7| Usually not busy | Sunday | People typically spend 30 min here | ChIJHSD5vb\_NHkcRI6Yvq0Hqqto | Amrit Oriental Food | Grochowska 207, Warszawa |
|    10|                12| Usually not busy | Sunday | People typically spend 30 min here | ChIJHSD5vb\_NHkcRI6Yvq0Hqqto | Amrit Oriental Food | Grochowska 207, Warszawa |
|    11|                19| Usually not busy | Sunday | People typically spend 30 min here | ChIJHSD5vb\_NHkcRI6Yvq0Hqqto | Amrit Oriental Food | Grochowska 207, Warszawa |

Scripts
=======

To use scripts on your own, get a Google Maps API key <https://developers.google.com/places/web-service/get-api-key>

> Scripts used to download the data will be shared during the hackathon.
