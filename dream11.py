from itertools import combinations

class Player:
  def __init__(self, name, team, price, ptype):
    self.name = name
    self.team = team
    self.price = price
    self.ptype = ptype

players={}
players["rahul"] = Player("rahul", "KXIP", 11, "WK")
players["abd"] = Player("abd", "RCB", 10, "WK")
players["pooran"] = Player("pooran", "KXIP", 9, "WK")

players["dhooda"] = Player("dhooda", "KXIP", 8, "BAT")
players["kohli"] = Player("kohli", "RCB", 10.5, "BAT")
players["agarwal"] = Player("magarwal", "KXIP", 9.5, "BAT")
players["finch"] = Player("afinch", "RCB", 9, "BAT")
players["padikal"] = Player("dpadikkal", "RCB", 8.5, "BAT")
players["gayle"] = Player("gayle", "KXIP", 9, "BAT")

players["cmorris"] = Player("cmorris", "RCB", 9, "ALL")
players["wsundar"] = Player("wsundar", "RCB", 8.5, "ALL")
players["sdube"] = Player("sdube", "RCB", 8.5, "ALL")
players["gmaxwell"] = Player("gmaxwell", "KXIP", 8.5, "ALL")

players["ychahal"] = Player("ychahal", "RCB", 9, "BOW")
players["mshami"] = Player("mshami", "KXIP", 9, "BOW")
players["iudana"] = Player("iudana", "RCB", 8.5, "BOW")
players["nsaini"] = Player("nsaini", "RCB", 8.5, "BOW")
players["cjordan"] = Player("cjordan", "KXIP", 8.5, "BOW")
players["mashwin"] = Player("mashwin", "KXIP", 8, "BOW")
players["rbishnoi"] = Player("rbishnoi", "KXIP", 8.5, "BOW")
players["msiraj"] = Player("msiraj", "RCB", 8, "BOW")
players["asingh"] = Player("asingh", "KXIP", 8, "BOW")

addedPlayer = ["rahul", "kohli", "abd", "pooran", "dhooda", "agarwal", "finch",
              "padikal", "gayle", "cmorris", "wsundar", "sdube", "gmaxwell",
               "ychahal", "mshami", "iudana", "nsaini", "cjordan", "mashwin",
                "rbishnoi", "msiraj", "asingh"]

removePlayer = ["gmaxwell", "cjordan"]

willPlayPLayer = ["abd", "kohli"]

allPlayer = [x for x in addedPlayer if x not in removePlayer]

print(allPlayer)

kxipPlayer = list(filter(lambda x: players[x].team == "KXIP", allPlayer))
rcbPlayer = list(filter(lambda x: players[x].team == "RCB", allPlayer))

def typelist(ttype, arr):
    return list(filter(lambda x: players[x].ptype == ttype, arr))

def qualify(ttype):
    wkplayer = typelist("WK", ttype)
    batplayer = typelist("BAT", ttype)
    bowlplayer = typelist("BOW", ttype)
    allplayer = typelist("ALL", ttype)
    priceplayer = list(map(lambda x: players[x].price, ttype))
    if(len(wkplayer) >= 1 and len(batplayer) >= 3 and len(bowlplayer) >= 3 and len(allplayer) >= 1 and sum(priceplayer) <= float(100)):
        return True;
    return False;


def combTeam(a, b):
    print(a, b)
    for i in combinations(kxipPlayer, a):
        for j in combinations(rcbPlayer, b):
            team = list(set(i).union(set(j)))
            if qualify(team):
                for m in team:
                    print(players[m].name, players[m].ptype, players[m].team)
                print()

combTeam(7,4)
combTeam(4,7)
combTeam(6,5)
combTeam(5,6)
