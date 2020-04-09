<p align="right">
<img src="images/bricks.gif" width="300" height="270">
</p>

# NBA Shots Analysis: Can defense cause bricks?
**Ray Zhao**

### Table of Contents

* [Overview](#overview)
    * [Project Description](#description)
    * [Motivation](#Motivation)
* [Data](#data)
* [Analysis](#analysis)
* [Plots](#plots)
* [Hypothesis Testing](#testing)
* [Conclusion](#conclusion)

<a name="overview"></a>
## Overview

### Project Description

In the 2014-15 NBA Season, ...

### Motivation

In basketball, offense is often considered more important than defense ...


<a name="data"></a>
## Data

**Source:**
* Original CSV dataset obtained from [Kaggle](https://www.kaggle.com/dansbecker/nba-shot-logs). 
* Dataset consists of details on all shots taken in the 2014-15 NBA regular season from October to March

**Pipeline:**
* Dataset imported using Pandas CSV read.
* Removed rows containing missing information i.e. null values.
* Removed unnecessary features
* Checked for inconsistencies in data then removed records containing those values e.g.,
    * Negative values for touch time (seconds the ball is held before a shot)
    * Incorrectly recorded 2 and 3 point shots (where shot distance did not match point type)
* Converted game clock string into total seconds passed

**Cleaned Data:**
* Dataset contains 115,235 rows and 15 features

| Features Name    | Description                                                           | Datatype |
|:-----------------|:----------------------------------------------------------------------|----------|
| Game ID          | Unique 8 digit number assigned to each individual game                | int      |
| Shot Number      | The number of the shot the player as taken in that game               | int      |
| Period           | The period of the game, there are 4 Quarters (1-4) and Overtimes      | int      |
| Game Clock       | Total seconds that pass since the start of the game                   | int      |
| Shot Clock       | Time on the shot clock when the shot is taken (counts down from 24.0) | float    |
| Dribbles         | Number of dribbles before the shot                                    | int      |
| Touch Time       | Time in seconds that the ball is held before the shot                 | float    |
| Shot Distance    | Distance of the shot in feet                                          | float    |
| Close Def Dist   | Distance of the closest defender in feet                              | float    |
| Pts Type         | 2 point or 3 point shot                                               | int      |
| Shot Result      | The shot is 'made' or 'missed'                                        | string   |
| FGM              | Binary version of 'Shot Result', 1 for 'made' and 0 for 'missed'      | int      |
| PTS              | Points resulting from the shot, dependent on Pts Type and FGM         | int      |
| Closest Defender | Name of the closest defender                                          | string   |
| Player Name      | Name of the player that took the shot                                 | string   |


<a name="analysis"></a>
## Analysis

### Exploratory Data Analysis

In this dataset, there are 896 unique games with data on shots taken from 281 players. Of the total 115,235 shots, 73.7% are 2 point shots while 26.3% are 3 point shots showing how in the 2014-15 NBA season 2 point shots were the majority of shots taken.

|                | Total Shots   |   2 Point Shots   |  3 Point Shots |
|:---------------|:-------------:|:-----------------:|:--------------:|
| Count          | 115,235       |       84,877      |         30,358 |
| % Made         | 44.3          | 48.6              | 36.1           |
| % Missed       | 53.4          | 51.4              | 63.9           |
| Most Taken By  | James Harden  | Lamarcus Aldrigde |  Stephen Curry |
| Most Made By   | Stephen Curry |   Nikola Vucevic  |  Stephen Curry |
| Most Missed By | James Harden  | Lamarcus Aldridge | Damian Lillard |

**Fun Facts:**
* Most Taken/Made Shots with shot clock under 4 seconds: Lebron James
* Most Shots Taken in One Game: Russell Westbrook with 37 shots
* Most Dribbles before a shot: Mo Williams with 32 dribbles
* Highest Shot Making Percentage (FG%): Deandre Jordan with 72.8%
* “Best Defender”: Most Occurences of being 4 ft away from the shot
    * The defensive rustle player: Pau Gasol
    * Most shots resulting in a miss: Draymond Green

**More Stuff:**
* ...?

<a name="plots"></a>
## Plots

<p align='center'>
<img src="images/dribbletime.png"> 
</p>



<p align='center'>
<img src="images/shotdisthist.png"> 
</p>

<p align='center'>
<img src="images/shotclockhist.png"> 
</p>

<p align='center'>
<img src="images/defdistscatter.png"> 
</p>


<a name="testing"></a>
## Hypothesis Testing

...


<a name="conclusion"></a>
## Conclusion

...
