import json
import pandas as pd
from itertools import combinations
import time


class CreateDreamTeam(object):
    def __init__(self, json_path='player.json'):
        self.__json_path = json_path
        self.__json_data = None
        self.init_json()
        self.create_team_wise_players()
        self.__df_data = []
        self.__total_qualifying_teams = 0
        self.__df = None

    def init_json(self):
        self.__json_data = json.load(open(self.__json_path))
        self.__player_data = self.__json_data['players_list']
        # print(self.__player_data)
        self.__teams = self.__json_data['teams']

    def create_team_wise_players(self):
        self.__team_a = []
        self.__team_b = []
        for val in self.__player_data:
            if val['team'] == self.__teams[0]:
                tmp_json = {}
                tmp_json['name'] = val['name']
                tmp_json['id'] = val['id']
                self.__team_a.append(tmp_json)
            elif val['team'] == self.__teams[1]:
                tmp_json = {}
                tmp_json['name'] = val['name']
                tmp_json['id'] = val['id']
                self.__team_b.append(tmp_json)
            else:
                raise ValueError("Wrong list of teams or team of the player")

    def __typelist(self, ttype, names_list):
        # return list(filter(lambda x: players[x].ptype == ttype, names_list))
        ret_list = []
        for val in names_list:
            if self.__player_data[val['id'] - 1]['type'].lower() == ttype.lower():
                ret_list.append(val)
        return ret_list

    def __get_total_price(self, names_list):
        total = 0
        for val in names_list:
            total += self.__player_data[val['id'] - 1]['value']
        return total

    def __qualify(self, val_list):
        # print(len(val_list))
        # names_list = self.__get_names_list(val_list)
        names_list = val_list
        wkplayer = self.__typelist("WK", names_list)
        batplayer = self.__typelist("BAT", names_list)
        bowlplayer = self.__typelist("BOWL", names_list)
        allplayer = self.__typelist("ALL", names_list)
        # priceplayer = list(map(lambda x: players[x].price, ttype))
        total = self.__get_total_price(names_list)
        # print(len(wkplayer), len(batplayer), len(bowlplayer), len(allplayer), total)
        # print(total)
        # exit(0)
        if (len(wkplayer) >= 1 and len(batplayer) >= 3 and len(bowlplayer) >= 3 and len(allplayer) >= 1 and total <= float(100)):
            return True;
        return False;

    def __get_names_list(self, obj_list):
        ret_list = []
        for val in obj_list:
            ret_list.append(val['name'])
        return ret_list

    def get_combination(self, team_a_count=6):
        t1 = time.time()
        team_b_count = 11 - team_a_count
        assert team_b_count > 0, "Team A count more than 10"
        for team_a_comb in combinations(self.__team_a, team_a_count):
            for team_b_comb in combinations(self.__team_b, team_b_count):
                # team = list(set(i).union(set(j)))
                # team = list(team_a_comb) + [i for i in list(team_b_comb) if i not in list(team_a_comb)]
                # print(team_a_comb, team_b_comb)
                team = list(team_a_comb)
                team.extend(list(team_b_comb))
                if self.__qualify(team):
                    self.__total_qualifying_teams += 1
                    # self.__df = self.__df.append(self.__get_names_list(team), ignore_index=True)
                    self.__df_data.append(self.__get_names_list(team))
        self.__df = pd.DataFrame(self.__df_data)
        t2 = time.time()
        print("Total time required to process: {} seconds".format(t2 - t1))
        print("Total number of teams qualified: {}".format(self.__total_qualifying_teams))

    def return_data(self):
        return self.__df

    def print_data(self):
        print(self.__df_data)

    def save_data(self):
        self.__df.to_csv('out.csv')


if __name__ == "__main__":
    obj = CreateDreamTeam()
    obj.get_combination(team_a_count=5)
    obj.save_data()
