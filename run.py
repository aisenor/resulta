import json
import urllib.request
import pprint
import datetime as dt

format = '%Y-%m-%d'
resp = []

# I extracted these three lines to allow the helper method to access
# team_rankings_data instead of having it request and open every time
team_rankings = "https://delivery.chalk247.com/team_rankings/NFL.json?api_key=74db8efa2a6db279393b433d97c2bc843f8e32b0"
url_tr = urllib.request.urlopen(team_rankings)
team_rankings_data= json.loads(url_tr.read().decode())

# This prevents the pprint function from sorting elements alphabetically
# to better match the provided example output
pprint.sorted = lambda x, key=None: x

"""
accept_input continues to prompt the user for a properly formatted
date until one is obtained. Format can be adjusted in the format
variable above

parameters:
string - user input

return:
date - properly formatted date
"""
def accept_input(string):
    while True:
        try:
            date = input("Enter {} (YYYY-MM-DD): ".format(string))
            dt.datetime.strptime(date, format)
        except ValueError:
            print('The date you entered is not formatted correctly')
            continue
        else:
            return date
            break

"""
This helper method parses the team rankings data to get the
rank and points associated with a team id

parameters:
id - team id

return:
dictionary containing rank and adjusted points assocaited with given team id
"""
def team_rank(id):
    for team in team_rankings_data['results']['data']:
        if team['team_id'] == id:
            return {
                "rank": team['rank'],
                "points": team['adjusted_points']
            }

def main():
    start_date = accept_input("start date")
    end_date = accept_input("end date")

    scoreboard = "https://delivery.chalk247.com/scoreboard/NFL/{}/{}.json?api_key=74db8efa2a6db279393b433d97c2bc843f8e32b0".format(start_date, end_date)
    url_scoreboard = urllib.request.urlopen(scoreboard)
    scoreboard_data = json.loads(url_scoreboard.read().decode())

    for date in scoreboard_data['results']:
        try:
            for id in scoreboard_data['results'][date]['data']:
                event = {}
                event_data = scoreboard_data['results'][date]['data'][id]

                date_time_obj = dt.datetime.strptime(event_data['event_date'], '%Y-%m-%d %H:%M')
                away_rank_points = team_rank(event_data['away_team_id'])
                home_rank_points = team_rank(event_data['home_team_id'])

                event = {
                    "event_id": event_data['event_id'],
                    "event_date": date_time_obj.strftime('%d-%m-%Y'),
                    "event_time": date_time_obj.strftime('%H:%M'),
                    "away_team_id": event_data['away_team_id'],
                    "away_nick_name": event_data['away_nick_name'],
                    "away_city": event_data['away_city'],
                    "away_rank": away_rank_points['rank'],
                    "away_rank_points": away_rank_points['points'],
                    "home_team_id": event_data['home_team_id'],
                    "home_nick_name": event_data['home_nick_name'],
                    "home_city": event_data['home_city'],
                    "home_rank": home_rank_points['rank'],
                    "home_rank_points": home_rank_points['points']
                }
                resp.append(event)
        except:
            # In case there is no entry for a given date
            continue

    pprint.pprint(resp)

if __name__ == "__main__":
    main()
