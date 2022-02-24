def calculate_no_of_ways(attendance_order,i,count):
    global n,k ,rejection_from_accepted,accepted
    if i==n:
        if attendance_order[i-1]=='a':
            rejection_from_accepted+=1
        accepted+=1
        return
    temp=attendance_order
    temp+='a'
    if not count+1>=k:
        calculate_no_of_ways(temp,i+1,count+1)
    temp=attendance_order
    temp+='p'
    calculate_no_of_ways(temp,i+1,0)

# total no of classes.
n=int(2)

# cannot miss more than 4 classes
k = int(4)

# graduation class missed
rejection_from_accepted=0
# no of ways
accepted=0


calculate_no_of_ways('',0,0)

# no of ways to attend classes
print(accepted)
#probablitly
print(str(rejection_from_accepted)+ '/'+ str(accepted))