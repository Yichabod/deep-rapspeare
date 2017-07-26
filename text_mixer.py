with open('Users/JamieFoxx/Desktop/bars.txt') as f:  #add the pathfile to your Rap Lyrics
    bars = f.readlines()
    bars = [x.strip() for x in bars] #strip removes the '\n' and other stuff for nice formatting
with open('/Users/JamieFoxx/Desktop/Shakespeare.txt') as g: #pathfile to your Shakespeare
    poetry = g.readlines()
    poetry = [y.strip() for y in poetry] 
both = []
for z in range(len(poetry)):
    bars[z] += '\n'
    poetry[z] += '\n'
    both.append(bars[z])
    both.append(poetry[z])
with open('/Users/JamieFoxx/Desktop/RapSpeare.txt','w') as h: #pathfile to the name of the mixed text
    h.writelines(both)
