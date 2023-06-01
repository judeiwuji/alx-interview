#!/usr/bin/python3
"""Module: Prime Game"""


def isPrime(d):
    """Checks primality of a number"""
    if d <= 1:
        return False
    if d == 2 or d == 3:
        return True
    if d % 2 == 0 or d % 3 == 0:
        return False
    for n in range(2, int(d ** 0.5)):
        if d % n == 0:
            return False
    return True


def getMultiples(d, n):
    """Returns: multiples of a number"""
    return [i for i in range(d, n+1, d)]


def getNextPlayer(player):
    """Returns: next game player"""
    return 0 if player == 1 else 1


def getWinner(players):
    """Returns: the name of the game winner"""
    if players[0]['wins'] == players[1]['wins']:
        return None

    return players[0]['name'] if players[0]['wins'] >\
        players[1]['wins'] else players[1]['name']


def isWinner(x, nums):
    """Determines game winner

    Args:
      x: number of rounds
      nums: list of numbers

    Returns: A boolean
    """
    if x > len(nums):
        return None
    player = 0
    players = {
        0: {
            'name': 'Maria',
            'wins': 0
        },
        1: {
            'name': 'Ben',
            'wins': 0
        }
    }
    round = 0

    while round < x:
        player = 0
        game = nums[round]
        board = [i for i in range(1,  game + 1)]

        while len(board) > 0:
            primes = [d for d in board if isPrime(d)]
            if len(primes) == 0:
                player = getNextPlayer(player)
                players[player]['wins'] += 1
                break
            pick = primes[0]
            multiples = getMultiples(pick, game)
            board = list(set(board).difference(multiples))
            player = getNextPlayer(player)
        round += 1
    return getWinner(players)
