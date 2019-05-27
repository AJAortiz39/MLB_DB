
import sqlite3

def create_db(fn, dbname):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    sql1 = "create table MLBBatters (name text, team text, position text, games int, ab int, runs int, hits int, doubles int, triples int, hr int, rbi int, sb int, cs int, bb int, so int, sh int, sf int, hbp int, avg float, obp float, slg float, ops float)"
    cursor.execute(sql1)
    with open(fn, 'r', encoding="UTF-8") as f:
        for line in f:
            if not line.startswith("Player"):
                line = line.replace("\n", "")
                L = line.split(',')
                name = L[0]
                team = L[1]
                position = L[2]
                games = L[3]
                ab = L[4]
                runs = L[5]
                hits = L[6]
                doubles = L[7]
                triples = L[8]
                hr = L[9]
                rbi = L[10]
                sb = L[11]
                cs = L[12]
                bb = L[13]
                so = L[14]
                sh = L[15]
                sf = L[16]
                hbp = L[17]
                avg = L[18]
                obp = L[19]
                slg = L[20]
                ops = L[21]
                sql2 = "INSERT INTO MLBBatters (name, team, position, games, ab, runs, hits, doubles, triples, hr, rbi, sb, cs, bb, so, sh, sf, hbp, avg, obp, slg, ops) VALUES (:name, :team, :position, :games, :ab, :runs, :hits, :doubles, :triples, :hr, :rbi, :sb, :cs, :bb, :so, :sh, :sf, :hbp, :avg, :obp, :slg, :ops)"
                cursor.execute(sql2, {"name":name, "team":team, "position":position, "games":games, "ab":ab, "runs":runs, "hits":hits, "doubles":doubles, "triples":triples, "hr":hr, "rbi":rbi, "sb":sb, "cs":cs, "bb":bb, "so":so, "sh":sh, "sf":sf, "hbp":hbp, "avg":avg, "obp":obp, "slg":slg, "ops":ops})
    conn.commit()
    conn.close()



def main():
    create_db("mlb-player-stats-Batters.csv", "MLB_Batters.db")
main()
