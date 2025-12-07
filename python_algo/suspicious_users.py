def find_suspicious_users(logs) -> list[string]:
    user_logs = {} # {alice:[10,20,50] , bob:[30,95,120],charlie:[15,40,65]}
    for user,time in logs: # ["alice", 10]
        if user not in user_logs:
            user_logs[user] = [] # {alice:}
        user_logs[user].append(time) # {alice:[10,20,30]}
    
    suspicious = []

    for user in user_logs:
        times = sorted(user_logs[user]) # sorted([10,20,50,70])
        for i in range (len(times)-2): # 0,2
            if times[i+2] - times[i]  <= 60:
                suspicious.append(user)
                break


    return suspicious
            





