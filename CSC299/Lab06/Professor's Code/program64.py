import csv

def read_heroes(filename="superheroes.csv"):
    columns = 'NAME,INTELLIGENCE,STRENGTH,SPEED,DURABILITY,POWER,COMBAT'.split(',')    
    heroes = []
    with open(filename) as myfile:
        reader = csv.reader(myfile)
        rows = [row for row in reader][1:]
        for row in rows:
            name = row[0]
            total_power = sum(map(int,row[1:]))
            item = (total_power, name)
            heroes.append(item)
        
        
        heroes.sort(reverse=True)
        # print heroes
        with open('ranking.csv','w') as myfile:
            writer = csv.writer(myfile)
            writer.writerow(['RANK','NAME','TOTAL_POWERS'])
            rank = 1
            for hero in heroes:
                (total_power, name) = hero
                
                writer.writerow([rank, name, total_power])
                rank +=1 

read_heroes()
