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

The goal for basketball is to win by making more shots and scoring more points than your opponent. The two biggest aspects of basketball are offense and defense, offense being the points your team scores and defense being the capability of stopping the opposing team from scoring. In the 2014-15 NBA season, let’s see if there was a difference in the distance of the closest defender in made and missed shots.

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

<a name="plots"></a>
## Plots

**Comparing the Number of Dribbles Against Time the Ball is Held:**
<p align='center'>
<img src="images/dribblesvstouchtime.png"> 

The number of dribbles and the amount of time a player touchs the ball before a shot are both key factors in scoring the basketball. Players will use dribbles to try to get around their defenders or to create space for a better opportunity for a shot. As one can see in the histograms above, players do not hold and dribble the ball for two long before passing. Most the time, if a player has the ball they will dribble leading to a linear relationship between dribbles and touch time. According to the scatterplot, neither dribbles or touch time affect the shot outcome. There are a few points where the ball is held for a long time with a low number of dribbles caused by situations where the player purposely runs down the shot clock so the last shot of a period which are often the most difficult leading to more missed shots.  
</p>

**Number of Shots Taken Throughout the Shot Clock:**
<p align='center'>
<img src="images/shotclockhist.png"> 

The shot clock is a 24 second countdown where one team has possession of the ball and resets if the possession of the ball is changed. In the two histograms above, the distribution of 2 point and 3 point shots are shown over the course of the shot clock counting down. Both distributions are relatively normal leading one to believe that most the time player choose to take the shot half through the shot clock which is common practice because they don't want to run out of time. Although shooting the ball early on is not encouraged by coachs, players will shoot the ball whenever they are open which leads to the peak of made shots in the 2 Point Clock Times. Those opportunities are created from steals or fast breaks, the players will get a shot with no defenders close by leading to a high percentage shot early in the shot clock. Other times the opposing team cause pressure causing a team to shot the ball with the shot clock closer to 0.  
</p>

**Number of 2 and 3 Point Shots Taken at All Distances:**
<p align='center'>
<img src="images/shotdisthist.png"> 

2 point shots comprise of the majority of the shots taken because they are closer in shot distance resulting in a higher field goal percentage. The shots taken in the 0-5 ft distance is the only area where there are more made shots than missed. Players will often try to take the closest shot possibly but sometimes that isn't possible leading to them to take the "midrange shot". The midrange shot the second peak ranging from 15-20 ft.

3 point shots are shots taken from a longer distance. The 3 point line on a NBA basketball court is a semicircle with the basket in the middle of the flat side. There are two set distances for a 3 point shot, the majority of the 3 point line is 23.75 ft away from the basket while the corners are flattened to be 22 ft away. This is why the 3 Point Shot Distances have two peaks.  
</p>

**Shot Distance and Shot Clock Compared to Closest Defender Distance:**
<p align='center'>
<img src="images/defdistscatter.png"> 

The biggest difference between a shot taken in a NBA game and practice shot is that there are defenders. In both scatterplots above, there is a large amount of made shots where the closest defender is far away caused by steals or fast breaks. Disregarding the shots were the defender is really far, the shot distance appears to be an important factor in if the shot is made or missed while the made and missed shots are evenly distributed thoughout the countdown of the shot clock. Which concurs with what was seen the the previous histograms.  
</p>

**2 and 3 Point Shots' Closest Defender Distances:**
<p align='center'>
<img src="images/twothreedefdist.png"> 

Looking at 2 and 3 point shots where the closest defender's distance was under 20 feet, it seems like for 2 point shots the smaller the distance of the closest defender the more likely the shot is to be missed. As the closest defender's distance increases, the number of made shots in this datasets either come very close or even overtake the missed shots. On the other hand in the 3 point shot histogram, the same conclusion cannot be drawn as easily. The distribution for made and missed shots are very similar.  
</p>

<a name="testing"></a>
## Hypothesis Testing

### The U-Test for 3 Point Shot Closest Defender Distance:

To test the hypothesis that closest defender distance is a factor in the 3 point shot outcome, we need to adopt a Null hypothesis.  The Null for the Mann–Whitney test is directly related to if a made or missed shot has a greater closest defender distance.

**Null Hypothesis:** The distance of the closest defender for missed three point shots are equally likely to be higher than for made three point shots as the other way around; i.e., 
  
P ( Missed Three Defender Distance} > Made Three Defender Distance ) = 0.5
  
As is usual, assuming this null hypothesis is true, the rank-sum statistic assumes a known distribution.   
`stats.mannwhitneyu(madedefdist, missdefdist, alternative='greater')`  
from the scipy stats package was run to find the p-value.

**p-value for missed def dist > made def dist was 5.2e-32.**  
The closest defender distance for a made shot is clearly greater than for a missed shot.


<a name="conclusion"></a>
## Conclusion

What did you learn about your data?

What did you learn about data science?

What advice would you give yourself?

Do you want to continue with this topic?

