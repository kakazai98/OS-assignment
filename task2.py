print ("enter number of processes : ")
n=int(input())
print ("enter Arival Time of processes : ")

temp_processes_AT = []
temp_processes_AT = list(input().split())

print ("enter Burst Time of prosesses : ")
temp_processes_BT = []
temp_processes_BT = list(input().split())


for i in range(n):
	temp_processes_AT[i]=int(temp_processes_AT[i])
	temp_processes_BT[i]=int(temp_processes_BT[i])

temp_processes_AT, temp_processes_BT = (list(t) for t in zip(*sorted(zip(temp_processes_AT, temp_processes_BT))))



processes_AT = []
processes_BT = []

TAT = []
WT = []

avg_ta_time = 0
avg_w_time = 0

i = 0

while(len(temp_processes_AT) != 0):
	processes_AT.insert(i,temp_processes_AT[0])
	processes_BT.insert(i,temp_processes_BT[0])
	if(i==0):	
		WT.insert(i,processes_AT[i])
	else:
		WT.insert(i,(processes_AT[i-1]+processes_BT[i-1])+(processes_AT[i]-processes_AT[i-1]-processes_BT[i-1]))
	TAT.insert(i,WT[i]+processes_BT[i])
	avg_ta_time += TAT[i]
	avg_w_time += WT[i]
	del temp_processes_AT[0]
	del temp_processes_BT[0]
	i = i + 1

avg_ta_time = float(avg_ta_time)/n
avg_w_time = float(avg_w_time)/n

print("Process \t Arrival Time \t Burst Time \t Waiting Time \t Turnaround Time \n") 
for l in range(n):
	print(str(l)+"\t\t"+str(processes_AT[l])+"\t\t"+str(processes_BT[l])+"\t\t"+str(WT[l])+"\t\t"+str(TAT[l])+"\n")




