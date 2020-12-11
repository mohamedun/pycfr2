import sys
import os
sys.path.insert(0,os.path.realpath('.'))
from pokergames import *
from pokercfr import *
from pokertrees import *

# def near(val, expected, distance=0.0001):
#     return val >= (expected - distance) and val <= (expected + distance)
#
# print ('Computing NE for Half-Street Kuhn poker')
#
# hskuhn = half_street_kuhn_rules()
# cfr = CounterfactualRegretMinimizer(hskuhn)
# iterations_per_block = 1000
# blocks = 10
# for block in range(blocks):
#     print ('Iterations: {0}'.format(block * iterations_per_block))
#     cfr.run(iterations_per_block)
#     result = cfr.profile.best_response()
#     print ('Best response EV: {0}'.format(result[1]))
#     print ('Total exploitability: {0}'.format(sum(result[1])))
# print (cfr.profile.strategies[0].policy)
#
# print (cfr.profile.strategies[0].policy)
# print (cfr.profile.strategies[1].policy)
# print (cfr.counterfactual_regret)
# print ('Verifying P1 policy')
# assert(near(cfr.profile.strategies[0].policy['Q:/:'][CALL], 2.0 / 3.0, 0.01))
# assert(near(cfr.profile.strategies[0].policy['Q:/:'][RAISE], 1.0 / 3.0, 0.01))
# assert(near(cfr.profile.strategies[0].policy['K:/:'][CALL], 1, 0.01))
# assert(near(cfr.profile.strategies[0].policy['K:/:'][RAISE], 0, 0.01))
# assert(near(cfr.profile.strategies[0].policy['A:/:'][CALL], 0, 0.01))
# assert(near(cfr.profile.strategies[0].policy['A:/:'][RAISE], 1.0, 0.01))
# print ('Verifying P2 policy')
# assert(near(cfr.profile.strategies[1].policy['Q:/r:'][FOLD], 1.0, 0.01))
# assert(near(cfr.profile.strategies[1].policy['Q:/r:'][CALL], 0, 0.01))
# assert(near(cfr.profile.strategies[1].policy['K:/r:'][FOLD], 2.0 / 3.0, 0.01))
# assert(near(cfr.profile.strategies[1].policy['K:/r:'][CALL], 1.0 / 3.0, 0.01))
# assert(near(cfr.profile.strategies[1].policy['A:/r:'][FOLD], 0, 0.01))
# assert(near(cfr.profile.strategies[1].policy['A:/r:'][CALL], 1.0, 0.01))
#

import time

# t0 = time.time()
#
#
# print ('Computing NE for Leduc poker')
# leduc = leduc_rules()
# cfr = CounterfactualRegretMinimizer(leduc)
# print(len(cfr.profile.strategies[1].policy.keys()))
# iterations_per_block = 100
# blocks = 10
# for block in range(blocks):
#     print ('Iterations: {0}'.format(block * iterations_per_block))
#     cfr.run(iterations_per_block)
#     result = cfr.profile.best_response()
#     print ('Best response EV: {0}'.format(result[1]))
#     print ('Total exploitability: {0}'.format(sum(result[1])))
# print(cfr.profile.expected_value())
#
# t1 = time.time()
#
# print('Total time spent is {0}'.format(t1-t0))
# print('Time per 1000 iteration is {0}'.format(((t1-t0)*1000.0)/(block * iterations_per_block)))
#

print('Computing Mo Game')
mo_ruleset = mo_rules()
cfr = PublicChanceSamplingCFR(mo_ruleset)
print(len(cfr.profile.strategies[1].policy.keys()))
t0 = time.time()
iterations_per_block = 2
blocks = 20
for block in range(blocks):
    print ('Iterations: {0}'.format(block * iterations_per_block))
    cfr.run(iterations_per_block)
    result = cfr.profile.best_response()
    print ('Best response EV: {0}'.format(result[1]))
    print ('Total exploitability: {0}'.format(sum(result[1])))
print(cfr.profile.expected_value())
t1 = time.time()
print(t1-t0)
# # load first player strategy
# s0 = Strategy(0)
# s0.load_from_file('strategies/leduc/0.strat')
#
# # load second player strategy
# s1 = Strategy(1)
# s1.load_from_file('strategies/leduc/1.strat')
#
# # Create a strategy profile for this game
# profile = StrategyProfile(rules, [s0,s1])
#
# ev = profile.expected_value()
# print(ev)
