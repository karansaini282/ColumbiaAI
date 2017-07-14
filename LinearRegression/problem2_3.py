import csv
import decimal
with open('input2.csv', newline='') as csvfile:
    sum_x1=0
    sum_x2=0
    sum_x3=0
    count=0
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    file1=list(spamreader)            
    for i in range(len(file1)):
        row=file1[i]
        items_string=row[0]
        items=items_string.split(',')
        sum_x1+=float(items[0])
        sum_x2+=float(items[1])
        sum_x3+=float(items[2])
        count+=1
    avg_x1=sum_x1/count
    avg_x2=sum_x2/count
    avg_x3=sum_x3/count
    diff_x1=0
    diff_x2=0
    diff_x3=0
    for i in range(len(file1)):
        row=file1[i]
        items_string=row[0]
        items=items_string.split(',')        
        diff_x1+=(avg_x1-float(items[0]))**2
        diff_x2+=(avg_x2-float(items[1]))**2
        diff_x3+=(avg_x3-float(items[2]))**2
    sd_x1=(diff_x1/count)**0.5
    sd_x2=(diff_x2/count)**0.5
    sd_x3=(diff_x3/count)**0.5
    data=[]
    for i in range(len(file1)):
        row=file1[i]
        items_string=row[0]
        items=items_string.split(',')
        new_x1=(float(items[0])-avg_x1)/sd_x1
        new_x2=(float(items[1])-avg_x2)/sd_x2
        new_x3=(float(items[2])-avg_x3)/sd_x3
        data.append([new_x1,new_x2,new_x3])
    alpha=[0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10,15]
    for i in range(len(alpha)):
        b_0=0
        b_age=0
        b_weight=0
        for j in range(100):
            diff_b_0=0
            diff_b_age=0
            diff_b_weight=0
            for k in range(len(data)):
                diff_b_age+=(b_0+b_age*data[k][0]+b_weight*data[k][1]-data[k][2])*data[k][0]
                diff_b_weight+=(b_0+b_age*data[k][0]+b_weight*data[k][1]-data[k][2])*data[k][1]
                diff_b_0+=b_0+b_age*data[k][0]+b_weight*data[k][1]-data[k][2]
            b_0=b_0-(diff_b_0*alpha[i]/(count+1))
            b_age=b_age-(diff_b_age*alpha[i]/(count+1))
            b_weight=b_weight-(diff_b_weight*alpha[i]/(count+1))
        with open('output2.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile, lineterminator='\n', delimiter=',', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([alpha[i],100,b_0,b_age,b_weight])
            
            
