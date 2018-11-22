print ("enter number of processes : ")
n=int(input())
print ("enter Arival Time of processes : ")

processes_AT = []
processes_AT = list(input().split())

print ("enter Burst Time of prosesses : ")
processes_BT = []
processes_BT = list(input().split())

for i in range(n):
	processes_AT[i]=int(processes_AT[i])
	processes_BT[i]=int(processes_BT[i])

processes_AT, processes_BT = (list(t) for t in zip(*sorted(zip(processes_AT, processes_BT))))

WT = []
TAT = []
avg_ta_time = 0
avg_w_time = 0

WT.insert(0,processes_AT[0])
TAT.insert(0,processes_BT[0]+WT[0])

timer = TAT[0]

for key in range(1,n):
	while processes_AT[key]!=timer:
		timer = timer + 1
	WT.insert(key,timer)
	TAT.insert(key,WT[key]+processes_BT[key])
	timer = TAT[key]
	avg_w_time = avg_w_time + WT[key]
	avg_ta_time = avg_ta_time + TAT[key]
avg_w_time = float(avg_w_time)/n
avg_ta_time = float(avg_ta_time)/n

print("Process \t Arrival Time \t Burst Time \t Waiting time \t Turnaround Time \n")
for i in range(n):
	print(str(i)+"\t\t"+str(processes_AT[i])+"\t\t"+str(processes_BT[i])+"\t\t"+str(WT[i])+"\t\t"+str(TAT[i])+"\n")

print("Average Waiting Time = ",avg_w_time)
print("Average Turnaround Time = ",avg_ta_time)



