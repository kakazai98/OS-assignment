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

Final_AT = []
Final_BT = []
 
TAT = []
WT = []

avg_ta_time = 0
avg_w_time = 0

timer = 0

i = 0
m = 0
k = n
j = 0

print("Process \t Arrival Time \t Burst Time \t Waiting Time \t Turnaround Time \n") 



while(i != n):
	while j < k:
		if(temp_processes_AT[j] == timer):
			processes_AT.insert(m,temp_processes_AT[0])
			processes_BT.insert(m,temp_processes_BT[0])
			Final_AT.insert(m,temp_processes_AT[0])
			Final_BT.insert(m,temp_processes_BT[0])
			del temp_processes_AT[0]
			del temp_processes_BT[0]
			k = k -1
			m = m + 1
			processes_BT, processes_AT = (list(t) for t in zip(*sorted(zip(processes_BT,processes_AT))))
		else:
			j = j + 1

	p = 0
	while p<len(processes_AT):
		print(str(processes_AT[p])+"\t"+str(processes_BT[p]))				
		p = p + 1
	print("timer = "+str(timer))				
	j = 0	
	timer = timer + 1
	if(len(processes_BT) != 0):	
		processes_BT[0] -= 1		
		if(processes_BT[0]==0):
			TAT.insert(i,timer-processes_AT[0])			
			if(i==0):	
				WT.insert(i,processes_AT[0])
			else:
				WT.insert(i,(TAT[i]-Final_BT[Final_AT.index(processes_AT[0])]))			
			avg_ta_time += TAT[i]
			avg_w_time += WT[i]
			print(str(i)+"\t\t"+str(processes_AT[0])+"\t\t"+str(Final_BT[Final_AT.index(processes_AT[0])])+"\t\t"+str(WT[i])+"\t\t"+str(TAT[i])+"\n")
			i = i + 1	
			del processes_BT[0]
			del processes_AT[0]

avg_ta_time = float(avg_ta_time)/n
avg_w_time = float(avg_w_time)/n

print("Average Waiting Time = "+str(avg_w_time))
print("Average Turnaround Time = "+str(avg_ta_time))



