import json


def read_table(table_path):
     with open(table_path, 'r') as f:
         content=f.readlines()
         AttackSpeedStr = content[0].strip('\n').split(',')[1:]
         FramesStr = content[1].strip('\n').split(',')[1:]
         AttackIntervalStr = content[2].strip('\n').split(',')[1:]

         d = [
             {
             "AttackSpeed": float(AttackSpeedStr[i]),
             "Frames": int(FramesStr[i]),
             "AttackInterval": float(AttackIntervalStr[i])}


             for i in range(len(AttackSpeedStr))]

     return json.dumps(d)



if __name__ == '__main__':
    r = read_table("data.csv")
    with open("save.json", 'w') as f:
        f.writelines(r)