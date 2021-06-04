# Swiping Hell
As of 2021, the largest dating apps by user count all use a "swiping" mechanic where you decide whether someone is 👍 or 👎. If you both 👍 each other, then you "match" and can actually message each other.

Heterosexual men get an extremely low match rate on these apps, which is seems to lead to a positive feedback loop wherein men 👍 nearly everyone as quickly as possible, which lowers their match rate further, to which men respond by 👍ing even more profligately. Instead of carefully choosing whom to 👍, a man instead defers all the real "choosing" work to the post-match phase, spending mental effort only on the tiny fraction of women who have 👍'd him back.

But that raises a question: is this *optimal* behavior, or is it a counterproductive reaction to the frustration of getting almost no matches?

This model attempts to answer that.

# Understanding the model

Look at the `find_a_date` function in [dates.py](dates.py) to understand the "core" of the model, and hopefully that will equip you to understand the details by reading the rest of the code.

# Select results

```
$ python3 dates.py
simulating SwipeEveryoneClassifier x 1000
100%|█████████████████████████████████████████████████████████████| 1000/1000 [00:00<00:00, 1056.10it/s]
mean people checked: 498.107
mean people swiped:  498.107
mean people chatted: 5.465
mean cost incurred:  546.5
simulating FastSwipeClassifier x 1000
100%|██████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 972.37it/s]
mean people checked: 499.858
mean people swiped:  275.358
mean people chatted: 3.256
mean cost incurred:  825.458
simulating SlowSwipeClassiifer x 1000
100%|██████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 994.94it/s]
mean people checked: 514.032
mean people swiped:  98.18
mean people chatted: 1.447
mean cost incurred:  5285.02
```
