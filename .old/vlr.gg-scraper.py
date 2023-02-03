from bs4 import BeautifulSoup
import requests, numpy as np, pandas as pd
from time import sleep

url = "https://www.vlr.gg/112334/optic-gaming-vs-funplus-phoenix-valorant-champions-tour-stage-2-masters-copenhagen-lbf"

num_games = 5
current_map = 0
sum_scores = -1
game_has_ended = False

oddsA, oddsB, match_scores, rounds = [], [], [], []
while True:
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    try:
        score = soup.find_all("div", style="margin-right: 12px;")
        teamA_scores = []
        for i in range(num_games):
            teamA_scores.append(float(score[i].text))

        score = soup.find_all("div", style="margin-left: 8px;")
        teamB_scores = []
        for i in range(num_games):
            teamB_scores.append(float(score[i].text))
    except IndexError:
        print("\nMatch has ended\n")
        break
        


    current_map = max([len(np.where(np.array(teamA_scores)!=0)[0]), len(np.where(np.array(teamB_scores)!=0)[0])]) 
    if current_map ==0: # while the score of the first map is 0:0 the current map would be equal to 0
        current_map = 1

    if sum(teamA_scores)+sum(teamB_scores) != sum_scores:
        teams = soup.find_all("span", class_="match-bet-item-team") # creates a list of the team names 
        teamA = teams[0].text
        teamB = teams[1].text
        oddA = soup.find("span", class_="match-bet-item-odds mod-up mod-1").text
        oddB = soup.find("span", class_= "match-bet-item-odds mod-down mod-2").text
        oddsA.append(oddA)
        oddsB.append(oddB)
        match_score = f"{int(teamA_scores[current_map-1])} : {int(teamB_scores[current_map-1])}"
        match_scores.append(match_score)
        rounds.append(sum(teamA_scores)+sum(teamB_scores))


    dict = {"Map":current_map, "Round":rounds, "Map Score":match_scores, teamA:oddsA, teamB:oddsB}
    df = pd.DataFrame(dict)
    if sum(teamA_scores)+sum(teamB_scores) != sum_scores:
        sum_scores = sum(teamA_scores)+sum(teamB_scores)
        df.to_csv(f"{teamA} vs {teamB}")
        print()
        print(df)
    



    



