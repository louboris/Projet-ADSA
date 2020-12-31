import numpy
from random import randint

#STEP 1

#Question 1
examplePlayer = {"John": 0}

#print(examplePlayer)


#Question 2
def TournamentCreation():
    nbPlayers = 100
    Ranking = {"P{}".format(i): 0 for i in range(1, nbPlayers + 1)}
    return (Ranking)


#Question 3
def randScore(nbGames):
    score = 0
    while nbGames > 0:
        score += randint(0, 12)
        nbGames -= 1
    score = round(score / 3, 1)
    return score


#Question 4
def ScoreUpdate(CurrentGame, nbGames):
    for i in range(len(CurrentGame)):
        CurrentGame[list(CurrentGame)[i]] = CurrentGame[list(
            CurrentGame)[i]] + randScore(nbGames)
    print("Here is the updated score at the end of the game: ")
    print(CurrentGame)
    return CurrentGame


#Question 5
def CreateRandomGame(Ranking, nbGames):
    print("This Game is composed of the following Players:")
    CurrentGame = {}
    for i in range(10):
        rand = randint(0, len(Ranking) - 1)
        CurrentGame.update({list(Ranking)[rand]: Ranking[list(Ranking)[rand]]})
        Ranking.pop(list(Ranking)[rand])
    printPlayersScore(CurrentGame)
    ScoreUpdate(CurrentGame, nbGames)
    Ranking.update(CurrentGame)
    return Ranking


#Question 6
#Ranking = dict(sorted(Ranking.items(), key=lambda item: item[1], reverse=True))
def CreateRankingGame(Ranking, nbGames):
    print("This Game is composed of the following Players:")
    CurrentGame = {}
    for i in range(10):
        CurrentGame.update({list(Ranking)[0]: Ranking[list(Ranking)[0]]})
        Ranking.pop(list(Ranking)[0])
    printPlayersScore(CurrentGame)
    ScoreUpdate(CurrentGame, nbGames)
    Ranking.update(CurrentGame)
    return Ranking


#Question 7
def DropLast10(Ranking):
    '''
    print("Last 10 players are: ")
    for i in range(len(Ranking)-10,len(Ranking)):
        r = i+1
        print("Position %s : "%r, list(Ranking)[i], "with a score of :", Ranking[list(Ranking)[i]])
    '''
    print("Removing the last 10 players from the tournament")
    for i in range(10):
        Ranking.pop(list(Ranking)[len(Ranking) - 1])


#Question 8
def printPlayers(Ranking):
    playerList = []
    for i in range(len(Ranking)):
        r = i + 1
        playerList.append(list(Ranking)[i])
    print(playerList)


def printPlayersScore(Ranking):
    for i in range(len(Ranking)):
        r = i + 1
        print(list(Ranking)[i], "with a score of :", Ranking[list(Ranking)[i]])


def Top10Rank(Ranking):
    for i in range(10):
        r = i + 1
        print("Position %s :" % r,
              list(Ranking)[i], "with a score of :", Ranking[list(Ranking)[i]])


def Step1():
    # This is the tournament initialization, 100 players will be created.
    print("Here are the 100 Players of our tournament: ")
    Ranking = TournamentCreation()
    printPlayers(Ranking)
    #While we have more than 10 players
    Phase = 1
    print("")
    while len(Ranking) > 10:
        input("Press enter to see next phase")
        print("PHASE %s ----------------------------------------------------" %
              Phase)
        print("The current TOP10 Players")
        Top10Rank(Ranking)
        print("----------------------------------------------------")
        #Find the number of games we need to create based on the number of players
        nbplayers = len(Ranking)
        nbgames = int(nbplayers / 10)
        print(
            "%s qualification games will be created because there are %s players left."
            % (nbgames, nbplayers))

        #Creating our differents games
        while nbgames > 0:
            print(
                "GAME %s ----------------------------------------------------: "
                % nbgames)
            Ranking = CreateRankingGame(Ranking, 3)
            nbgames -= 1

        #Sorting the Rank
        Ranking = dict(
            sorted(Ranking.items(), key=lambda item: item[1], reverse=True))

        #Droping the last 10 players
        DropLast10(Ranking)
        Phase += 1
        print("")
    print("----------------------------------------------------")
    print("Final TOP10 Players are:")
    Top10Rank(Ranking)

    print("")
    # Final Game
    print("FINAL GAME----------------------------------------------------")
    print("All score are now reset")
    for i in range(10):
        Ranking[list(Ranking)[i]] = 0
    CreateRankingGame(Ranking, 5)
    #Sorting the Rank
    Ranking = dict(
        sorted(Ranking.items(), key=lambda item: item[1], reverse=True))
    print("----------------------------------------------------")
    print("Our 10 best players are: ")
    Top10Rank(Ranking)
    print(randScore(3))


# STEP 2


def computeImpostors(m, graph):
    #We will first look at the have seen relation from the murdered player.
    for i in range(len(graph[m])):
        impos = []
        crew = []
        if graph[m][
                i] == 1:  #If the player have been seen by the murdered player
            print("If %i" % i, "is the first impostor: ")

            #Compute the players that this probable imposter has seen
            for j in range(len(graph[i])):
                if graph[i][j] == 1:
                    crew.append(j)

                    #Compute the player that might be the second imposter
                    for k in range(len(graph[j])):
                        if graph[j][k] == 1:
                            if k != i:
                                impos.append(k)
            print("Possible second impostors are:")
            print(impos)
            print("Possible crewmates are: ")
            print(crew)


def Step2():
    #Adjacency matrix of our Graph - This graph is representing the "have seen" relations between each playsers.
    graph = [[0, 1, 0, 0, 1, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
             [0, 1, 0, 1, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
             [1, 0, 0, 1, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
             [0, 0, 0, 1, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 1, 0, 0]]

    m = int(input("Who died this round ? "))
    computeImpostors(m, graph)


if __name__ == "__main__":
    Step1()
    Step2()
