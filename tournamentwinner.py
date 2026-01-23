HOME_TEAM_WON = 1

def tournamentwinner(competition,results):
    currentbestteam = ""
    score = {currentbestteam: 0}

    for idx, competitions in enumerate(competition):
        result = results[idx]
        hometeam,awayteam = competitions
        winningteam = hometeam if result ==HOME_TEAM_WON else awayteam

        updatescores(winningteam,3,score)

        if score[winningteam] > score[currentbestteam]:
            currentbestteam = winningteam
    return currentbestteam

def updatescores(team,points,scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points

print(tournamentwinner([['Python','C#'],['HTML','Python'],['C#','HTML']],[0,1,0]))