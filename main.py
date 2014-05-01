from random import shuffle
import warnings

from yaml import dump
from sklearn.datasets import load_svmlight_file
from utils.experiment import test

from ensemblers.adaboost import AdaBooster
from ensemblers.ogboost import OGBooster
from ensemblers.ocpboost import OCPBooster
from ensemblers.expboost import EXPBooster

from learners.sk_naive_bayes import NaiveBayes
from learners.perceptron import Perceptron
from learners.random_stump import RandomStump
from learners.decision_stump import DecisionStump
from learners.decision_tree import DecisionTree
from learners.knn import kNN
from learners.histogram import RNB
from learners.winnow import Winnow

warnings.filterwarnings("ignore", module="sklearn")


def loadData(filename):
    X, y = load_svmlight_file(filename)

    data = zip(X, y)
    shuffle(data)
    return data

if __name__ == "__main__":
    dataset = "heart.txt"
    m = 100
    data = loadData("data/" + dataset)
    accuracy, baseline = test(AdaBooster, NaiveBayes, data, m)
    print accuracy
    print baseline[-1]
    if True:
        weak_learner = "NaiveBayes"
        booster = "OzaBoost"
        results = {
            'm': m,
            'accuracy': accuracy,
            'baseline': baseline[-1],
            'booster': booster,
            'weak_learner': weak_learner,
        }
        f = open(booster + "_" + weak_learner + ".yml", 'w+')
        f.write(dump(results))
