from dataclasses import dataclass
from enum import Enum
import itertools
import numpy as np
import random
from tqdm import tqdm
from typing import *

class DateGoodness(Enum):
    GOOD = 'GOOD'
    BAD  = 'BAD'

class Accept(Enum):
    YES = 'YES'
    NO  = 'NO'

@dataclass(eq=True, frozen=True)
class Person:
    date_goodness: DateGoodness
    accept: Accept

GOOD_YES = Person(DateGoodness.GOOD, Accept.YES)
GOOD_NO  = Person(DateGoodness.GOOD, Accept.NO)
BAD_YES = Person(DateGoodness.BAD, Accept.YES)
BAD_NO  = Person(DateGoodness.BAD, Accept.NO)


POPULATION_COUNTS = {
    GOOD_YES : 1,
    BAD_YES  : 9,
    GOOD_NO  : 99,
    BAD_NO   : 891,
}

POPULATION = list(itertools.chain(*([typ]*ct for typ,ct in POPULATION_COUNTS.items())))

Cost = int

class SwipeEveryoneClassifier:
    cost: Cost = 0

    def classify(person: Person) -> DateGoodness:
        return DateGoodness.GOOD


class FastSwipeClassifier:
    cost: Cost = 1

    def classify(person: Person) -> DateGoodness:
        if person.date_goodness == DateGoodness.BAD:
            if random.random() < 0.5:
                return DateGoodness.BAD
            else:
                return DateGoodness.GOOD

        else:
            return DateGoodness.GOOD

class SlowSwipeClassiifer:
    cost: Cost = 10

    def classify(person: Person) -> DateGoodness:
        if person.date_goodness == DateGoodness.BAD:
            if random.random() < 0.1:
                return DateGoodness.GOOD
            else:
                return DateGoodness.BAD

        else:
            return DateGoodness.GOOD

class ChatClassifier:
    cost: Cost = 100

    def classify(person: Person) -> DateGoodness:
        return person.date_goodness

def find_a_date(population: List[Person], swipe_classifier) -> Tuple[int, int, int, Cost]:
    people_checked = 0
    people_swiped  = 0
    people_chatted = 0
    cost = 0

    # Work through the population of possible dates, looking for a person who
    # is both a "good date" AND who has 👍ed you back.
    for person in population:
        people_checked += 1
        cost += swipe_classifier.cost
        # Decide whether to 👍 or 👎
        if swipe_classifier.classify(person) == DateGoodness.BAD:
            continue

        # We 👍ed them!
        people_swiped += 1

        # Did the other party 👍 us?
        if person.accept == Accept.NO:
            continue

        # We matched! Engage in comparatively costly chat to see for sure whether
        # they're a good date.
        people_chatted += 1
        cost += ChatClassifier.cost
        if ChatClassifier.classify(person) == DateGoodness.BAD:
            continue

        # We found a good date! Report how much work it took to do so.
        return people_checked, people_swiped, people_chatted, cost

def simulate(swipe_classifier, count=1000):
    print('simulating', swipe_classifier.__name__, 'x', count)
    results = []
    for _ in tqdm(range(count)):
        random.shuffle(POPULATION)
        results.append(find_a_date(POPULATION, swipe_classifier))

    people_checked, people_swiped, people_chatted, cost = zip(*results)
    print('mean people checked:', np.mean(people_checked))
    print('mean people swiped: ', np.mean(people_swiped))
    print('mean people chatted:', np.mean(people_chatted))
    print('mean cost incurred: ', np.mean(cost))

simulate(SwipeEveryoneClassifier)
simulate(FastSwipeClassifier)
simulate(SlowSwipeClassiifer)
