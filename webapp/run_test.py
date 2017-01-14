from bayes import bayes
from interact_web import get_headlines
from interact_twitter import get_tweets
import csv




twits = ['Inside this mental hospital in Venezuela, psychiatric patients face shortages of food and medicine… ', 'RT  Showtime! #theapprentice ', 'RT  Andy Murray named BBC Sports Personality of the Year. 🏆 Details of all awards:  ', "Trump aide plays down prospect of upending 'one China' policy  ", 'RT  Congratulations Alistair Brownlee 🏆\n\nSecond place in BBC Sports Personality of the Year 2016. \n\n #SPOT…', 'RT  As they watch Donald #Trump’s transition to the White House, supporters say “We have to trust him.” ', "RT  It's history for Andy Murray!\n\nHe's the first person to win BBC's Sports Personality of the Year three times.\n\n🏆 Congratulati…", 'RT  What a year it has been for Nick Skelton! 🏆\n\nThird place in the BBC Sports Personality of the Year 2016. \n\n', '900,000 children have been displaced by the on-going war in South Sudan  ', 'BLT Prime review: Trump Hotel’s steakhouse does plenty of things right ', '"I love you." She had said it.\nAt first, he didn\'t say anything. Then, finally, he muttered, "Thank you."\n', "RT  We'll bring you the announcement live from  and have reaction from the award winners\n\n http…", 'RT  What an unbelievable and magical season they had!\n\n🏆 Congratulations Leicester City 🏆\n\n➡️  #LCFC #SPOT…', 'Denied justice, this Italian Renaissance painter channeled her rape into her art ', 'At Least 10 Die In Shootout At Crusader Castle In Jordan ']
    # twits = get_tweets()

webs = get_headlines()

with open("test") as f1:
    lines = [x.strip() for x in f1.readlines()]


f2 = open("test_results.csv", "w") 
f2cw = csv.writer(f2)
f2cw.writerow(["prior", "likelihood", "marginal", "posterior", "probability"])
for line in lines:
    f2cw.writerow(bayes(twits, webs, line))
