import Teams
import pandas as pd
from datetime import datetime
from basketball_reference_scraper.box_scores import get_box_scores
from basketball_reference_scraper.seasons import get_schedule

class BasketballReferenceAPI:
    def __init__(self):
        self.team_abb = Teams.TeamAbb

    def get_game(self, date, team1_abb, team2_abb):
        game_id=team1_abb+team2_abb+date.strftime('%Y%m%d')
        box_score = pd.DataFrame()
        for type in ['BASIC','ADVANCED']:
            new_box_score = get_box_scores(date.strftime('%Y-%m-%d'), team1_abb, team2_abb,
                                   period='GAME', stat_type=type)
            new_box_score=pd.concat([new_box_score[team1_abb], new_box_score[team2_abb]],keys=[team1_abb, team2_abb])
            box_score=box_score.append(new_box_score)
        box_score['GAME_ID']=game_id
        print(game_id)
        return box_score

    def get_season_box_scores(self, season):
        schedule = pd.DataFrame.from_dict(get_schedule(season, False))
        box_score=pd.DataFrame()
        for game in schedule.iterrows():
            home_team_abb = Teams.TeamAbb[game[1]['HOME'].upper()]
            visitor_team_abb = Teams.TeamAbb[game[1]['VISITOR'].upper()]
            new_box_score = self.get_game(game[1]['DATE'], visitor_team_abb, home_team_abb)
            pd.concat([box_score,new_box_score])
        return box_score
aaa=BasketballReferenceAPI()
aaa.get_season_box_scores(2024).to_csv('file1.csv')

