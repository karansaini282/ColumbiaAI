import csv
with open('input1.csv', newline='') as csvfile:
    b=0
    w1=0
    w2=0
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    file1=list(spamreader)
    while True:
        c=0            
        for i in range(len(file1)):            
            row=file1[i]
            items_string=row[0]
            items=items_string.split(',')
            yin=b+(w1*int(items[0]))+(w2*int(items[1]))
            if(yin>=0):
                y=1
            else:
                y=-1
            if(y!=int(items[2])):
                b=b+0.5*int(items[2])
                w1=w1+0.5*int(items[2])*int(items[0])
                w2=w2+0.5*int(items[2])*int(items[1])
                c=c+1
            with open('output1.csv', 'a') as csvfile:
                spamwriter = csv.writer(csvfile, lineterminator='\n', delimiter=',', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([w1,w2,b])                
        if c==0:
            break
    with open('output1.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, lineterminator='\n', delimiter=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([w1,w2,b])
