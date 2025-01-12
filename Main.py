import Teams
import pandas as pd
from datetime import datetime
from basketball_reference_scraper.box_scores import get_box_scores
from basketball_reference_scraper.seasons import get_schedule
schedule=pd.DataFrame.from_dict(get_schedule(2024,False))
for game in schedule.iterrows():
    home_team_abb= Teams.TeamAbb[game[1]['HOME'].upper()]
    visitor_team_abb= Teams.TeamAbb[game[1]['VISITOR'].upper()]
    box_score = get_box_scores(game[1]['DATE'].strftime('%Y-%m-%d'), visitor_team_abb, home_team_abb, period='GAME', stat_type='BASIC')
    print(box_score)



