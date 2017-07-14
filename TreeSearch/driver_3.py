import sys
import math
import time
import resource

start_time = time.time()

goal=[0,1,2,3,4,5,6,7,8]

def bfs(states):
    n=int(math.sqrt(len(states)))
    flag=True
    path_to_goal=[]
    cost_of_path=0
    nodes_expanded=0
    fringe_size=1
    max_fringe_size=1
    search_depth=0
    max_search_depth=0
    visited=[]
    visited_queue=[]
    queue=[{'state':states,'level':0,'action':'root'}]
    if states==goal:
        flag=False
    while(flag):
        nodes_expanded=nodes_expanded+1        
        fringe_size=len(queue)
        if(fringe_size>max_fringe_size):
            max_fringe_size=fringe_size
        current=queue.pop(0)
        visited.append(current['state'])
        visited_queue.append(current)
        index=current['state'].index(0)        
        initial=current['state']
        if initial==goal:
            flag=False
            search_depth=current['level']
            nodes_expanded=nodes_expanded-1
            fringe_size=fringe_size-1
        if(index>n-1):
            swap=index-n
            final=initial[:]
            temp=final[index]
            final[index]=final[swap]
            final[swap]=temp
            if final not in visited:
                queue.append({'state':final,'level':current['level']+1,'action':'Up'})                
                if(current['level']+1>max_search_depth):
                    max_search_depth=current['level']+1
        if(index<len(states)-n):            
            swap=index+n
            final=initial[:]
            temp=final[index]
            final[index]=final[swap]
            final[swap]=temp
            if final not in visited:
                queue.append({'state':final,'level':current['level']+1,'action':'Down'})                
                if(current['level']+1>max_search_depth):
                    max_search_depth=current['level']+1
        if(index%n!=0):
            swap=index-1
            final=initial[:]
            temp=final[index]
            final[index]=final[swap]
            final[swap]=temp
            if final not in visited:
                queue.append({'state':final,'level':current['level']+1,'action':'Left'})                
                if(current['level']+1>max_search_depth):
                    max_search_depth=current['level']+1
        if(index%n!=n-1):
            swap=index+1
            final=initial[:]
            temp=final[index]
            final[index]=final[swap]
            final[swap]=temp
            if final not in visited:
                queue.append({'state':final,'level':current['level']+1,'action':'Right'})                
                if(current['level']+1>max_search_depth):
                    max_search_depth=current['level']+1
    current2=visited_queue.pop()
    flag2=True
    while(flag2):
        cost_of_path=cost_of_path+1
        action=current2['action']
        path_to_goal.append(action)
        state=current2['state']
        final2=state[:]
        index2=current2['state'].index(0)
        if(action=='Up'):
            swap=index2+n
            temp=final2[index2]
            final2[index2]=final2[swap]
            final2[swap]=temp
        if(action=='Down'):
            swap=index2-n            
            temp=final2[index2]
            final2[index2]=final2[swap]
            final2[swap]=temp
        if(action=='Left'):
            swap=index2+1            
            temp=final2[index2]
            final2[index2]=final2[swap]
            final2[swap]=temp
        if(action=='Right'):
            swap=index2-1            
            temp=final2[index2]
            final2[index2]=final2[swap]
            final2[swap]=temp
        for x in visited_queue:
            if(x['state']==final2):
                current2=x                
                break
        #current_index = next(index for (index, d) in enumerate(visited_queue) if d['state'] == final)
        #current=visited_queue[current_index]
        if(current2['action']=='root'):
            flag2=False;
    path_to_goal.reverse()
    print ('cost_of_path:',cost_of_path)
    print ('path_to_goal:',path_to_goal)
    print ('nodes_expanded:',nodes_expanded)
    print ('fringe_size:',fringe_size)
    print ('max_fringe_size:',max_fringe_size)
    print ('search_depth:',search_depth)
    print ('max_search_depth:',max_search_depth)
    print ('running_time:',round(time.time() - start_time, 8))
    print('max_ram_usage:',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/float(1024))
    f = open('output.txt','w')
    f.write ('cost_of_path: '+str(cost_of_path)+'\n')
    f.write ('path_to_goal: '+str(path_to_goal)+'\n')
    f.write ('nodes_expanded: '+str(nodes_expanded)+'\n')
    f.write ('fringe_size: '+str(fringe_size)+'\n')
    f.write ('max_fringe_size: '+str(max_fringe_size)+'\n')
    f.write ('search_depth: '+str(search_depth)+'\n')
    f.write ('max_search_depth: '+str(max_search_depth)+'\n')
    f.write ('running_time: '+str(round(time.time() - start_time, 8))+'\n')
    f.write ('max_ram_usage: '+str(round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/float(1024),8)))
    f.close()

def dfs(states):
    n=int(math.sqrt(len(states)))
    flag=True
    path_to_goal=[]
    cost_of_path=0
    nodes_expanded=0
    fringe_size=1
    max_fringe_size=1
    search_depth=0
    max_search_depth=0
    visited=[]
    visited_queue=[]
    queue=[{'state':states,'level':0,'action':'root'}]
    if states==goal:
        flag=False
    while(flag):
        nodes_expanded=nodes_expanded+1        
        fringe_size=len(queue)
        if(fringe_size>max_fringe_size):
            max_fringe_size=fringe_size
        current=queue.pop(0)
        visited.append(current['state'])
        visited_queue.append(current)
        index=current['state'].index(0)        
        initial=current['state']
        if initial==goal:
            flag=False
            search_depth=current['level']
            nodes_expanded=nodes_expanded-1
            fringe_size=fringe_size-1
        if(index%n!=n-1):
            swap=index+1
            final=initial[:]
            temp=final[index]
            final[index]=final[swap]
            final[swap]=temp
            if final not in visited:
                queue.insert(0,{'state':final,'level':current['level']+1,'action':'Right'})                
                if(current['level']+1>max_search_depth):
                    max_search_depth=current['level']+1
        if(index%n!=0):
            swap=index-1
            final=initial[:]
            temp=final[index]
            final[index]=final[swap]
            final[swap]=temp
            if final not in visited:
                queue.insert(0,{'state':final,'level':current['level']+1,'action':'Left'})                
                if(current['level']+1>max_search_depth):
                    max_search_depth=current['level']+1
        if(index<len(states)-n):            
            swap=index+n
            final=initial[:]
            temp=final[index]
            final[index]=final[swap]
            final[swap]=temp
            if final not in visited:
                queue.insert(0,{'state':final,'level':current['level']+1,'action':'Down'})                
                if(current['level']+1>max_search_depth):
                    max_search_depth=current['level']+1
        if(index>n-1):
            swap=index-n
            final=initial[:]
            temp=final[index]
            final[index]=final[swap]
            final[swap]=temp
            if final not in visited:
                queue.insert(0,{'state':final,'level':current['level']+1,'action':'Up'})                
                if(current['level']+1>max_search_depth):
                    max_search_depth=current['level']+1
    current2=visited_queue.pop()
    flag2=True
    while(flag2):
        cost_of_path=cost_of_path+1
        action=current2['action']
        path_to_goal.append(action)
        state=current2['state']
        final2=state[:]
        index2=current2['state'].index(0)
        if(action=='Up'):
            swap=index2+n
            temp=final2[index2]
            final2[index2]=final2[swap]
            final2[swap]=temp
        if(action=='Down'):
            swap=index2-n            
            temp=final2[index2]
            final2[index2]=final2[swap]
            final2[swap]=temp
        if(action=='Left'):
            swap=index2+1            
            temp=final2[index2]
            final2[index2]=final2[swap]
            final2[swap]=temp
        if(action=='Right'):
            swap=index2-1            
            temp=final2[index2]
            final2[index2]=final2[swap]
            final2[swap]=temp
        for x in visited_queue:
            if(x['state']==final2):
                current2=x                
                break
        #current_index = next(index for (index, d) in enumerate(visited_queue) if d['state'] == final)
        #current=visited_queue[current_index]
        if(current2['action']=='root'):
            flag2=False;
    path_to_goal.reverse()
    print ('cost_of_path:',cost_of_path)
    print ('path_to_goal:',path_to_goal)
    print ('nodes_expanded:',nodes_expanded)
    print ('fringe_size:',fringe_size)
    print ('max_fringe_size:',max_fringe_size)
    print ('search_depth:',search_depth)
    print ('max_search_depth:',max_search_depth)
    print ('running_time:',round(time.time() - start_time, 8))
    print('max_ram_usage:',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/float(1024))
    f = open('output.txt','w')
    f.write ('cost_of_path: '+str(cost_of_path)+'\n')
    f.write ('path_to_goal: '+str(path_to_goal)+'\n')
    f.write ('nodes_expanded: '+str(nodes_expanded)+'\n')
    f.write ('fringe_size: '+str(fringe_size)+'\n')
    f.write ('max_fringe_size: '+str(max_fringe_size)+'\n')
    f.write ('search_depth: '+str(search_depth)+'\n')
    f.write ('max_search_depth: '+str(max_search_depth)+'\n')
    f.write ('running_time: '+str(round(time.time() - start_time, 8))+'\n')
    f.write ('max_ram_usage: '+str(round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/float(1024),8)))
    f.close()

def manhattan(states):
    n=int(math.sqrt(len(states)))
    i=0
    sum1=0
    for state in states:
        if state!=0:
            dif=abs(i-state)
            while(dif>=n):
                dif=dif-n
                sum1=sum1+1
            sum1=sum1+dif
        i=i+1
    return sum1
            

def ast(states):
    n=int(math.sqrt(len(states)))
    flag=True
    path_to_goal=[]
    cost_of_path=0
    nodes_expanded=0
    fringe_size=1
    max_fringe_size=1
    search_depth=0
    max_search_depth=0
    visited=[]
    whole=[states]
    visited_queue=[]
    queue=[{'state':states,'level':0,'action':'root','cost':manhattan(states)}]
    if states==goal:
        flag=False
    while(flag):
        queue = sorted(queue, key=lambda k: k['cost']) 
        nodes_expanded=nodes_expanded+1        
        fringe_size=len(queue)
        if(fringe_size>max_fringe_size):
            max_fringe_size=fringe_size
        current=queue.pop(0)
        visited.append(current['state'])
        visited_queue.append(current)
        index=current['state'].index(0)        
        initial=current['state']
        if initial==goal:
            flag=False
            search_depth=current['level']
            nodes_expanded=nodes_expanded-1
            fringe_size=fringe_size-1
        if(index>n-1):
            swap=index-n
            final=initial[:]
            temp=final[index]
            final[index]=final[swap]
            final[swap]=temp
            if final not in visited:
                if final not in whole:
                    whole.append(final)
                    queue.append({'state':final,'level':current['level']+1,'action':'Up','cost':manhattan(final)+current['level']+1})                
                    if(current['level']+1>max_search_depth):
                        max_search_depth=current['level']+1
                if final in whole:
                    for item in queue:
                        if item['state']==final:
                            if item['cost']>manhattan(final)+current['level']+1:
                                queue.remove(item)
                                queue.append({'state':final,'level':current['level']+1,'action':'Up','cost':manhattan(final)+current['level']+1})
                                break
                    
        if(index<len(states)-n):            
            swap=index+n
            final=initial[:]
            temp=final[index]
            final[index]=final[swap]
            final[swap]=temp
            if final not in visited:
                if final not in whole:
                    whole.append(final)
                    queue.append({'state':final,'level':current['level']+1,'action':'Down','cost':manhattan(final)+current['level']+1})                
                    if(current['level']+1>max_search_depth):
                        max_search_depth=current['level']+1
                if final in whole:
                    for item in queue:
                        if item['state']==final:
                            if item['cost']>manhattan(final)+current['level']+1:
                                queue.remove(item)
                                queue.append({'state':final,'level':current['level']+1,'action':'Down','cost':manhattan(final)+current['level']+1})
                                break
        if(index%n!=0):
            swap=index-1
            final=initial[:]
            temp=final[index]
            final[index]=final[swap]
            final[swap]=temp
            if final not in visited:
                if final not in whole:
                    whole.append(final)
                    queue.append({'state':final,'level':current['level']+1,'action':'Left','cost':manhattan(final)+current['level']+1})                
                    if(current['level']+1>max_search_depth):
                        max_search_depth=current['level']+1
                if final in whole:
                    for item in queue:
                        if item['state']==final:
                            if item['cost']>manhattan(final)+current['level']+1:
                                queue.remove(item)
                                queue.append({'state':final,'level':current['level']+1,'action':'Left','cost':manhattan(final)+current['level']+1})
                                break
        if(index%n!=n-1):
            swap=index+1
            final=initial[:]
            temp=final[index]
            final[index]=final[swap]
            final[swap]=temp
            if final not in visited:
                if final not in whole:
                    whole.append(final)
                    queue.append({'state':final,'level':current['level']+1,'action':'Right','cost':manhattan(final)+current['level']+1})                
                    if(current['level']+1>max_search_depth):
                        max_search_depth=current['level']+1
                if final in whole:
                    for item in queue:
                        if item['state']==final:
                            if item['cost']>manhattan(final)+current['level']+1:
                                queue.remove(item)
                                queue.append({'state':final,'level':current['level']+1,'action':'Right','cost':manhattan(final)+current['level']+1})
                                break
    current2=visited_queue.pop()
    flag2=True
    while(flag2):
        cost_of_path=cost_of_path+1
        action=current2['action']
        path_to_goal.append(action)
        state=current2['state']
        final2=state[:]
        index2=current2['state'].index(0)
        if(action=='Up'):
            swap=index2+n
            temp=final2[index2]
            final2[index2]=final2[swap]
            final2[swap]=temp
        if(action=='Down'):
            swap=index2-n            
            temp=final2[index2]
            final2[index2]=final2[swap]
            final2[swap]=temp
        if(action=='Left'):
            swap=index2+1            
            temp=final2[index2]
            final2[index2]=final2[swap]
            final2[swap]=temp
        if(action=='Right'):
            swap=index2-1            
            temp=final2[index2]
            final2[index2]=final2[swap]
            final2[swap]=temp
        for x in visited_queue:
            if(x['state']==final2):
                current2=x                
                break
        #current_index = next(index for (index, d) in enumerate(visited_queue) if d['state'] == final)
        #current=visited_queue[current_index]
        if(current2['action']=='root'):
            flag2=False;
    path_to_goal.reverse()
    print ('cost_of_path:',cost_of_path)
    print ('path_to_goal:',path_to_goal)
    print ('nodes_expanded:',nodes_expanded)
    print ('fringe_size:',fringe_size)
    print ('max_fringe_size:',max_fringe_size)
    print ('search_depth:',search_depth)
    print ('max_search_depth:',max_search_depth)
    print ('running_time:',round(time.time() - start_time, 8))
    print('max_ram_usage:',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/float(1024))
    f = open('output.txt','w')
    f.write ('cost_of_path: '+str(cost_of_path)+'\n')
    f.write ('path_to_goal: '+str(path_to_goal)+'\n')
    f.write ('nodes_expanded: '+str(nodes_expanded)+'\n')
    f.write ('fringe_size: '+str(fringe_size)+'\n')
    f.write ('max_fringe_size: '+str(max_fringe_size)+'\n')
    f.write ('search_depth: '+str(search_depth)+'\n')
    f.write ('max_search_depth: '+str(max_search_depth)+'\n')
    f.write ('running_time: '+str(round(time.time() - start_time, 8))+'\n')
    f.write ('max_ram_usage: '+str(round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/float(1024),8)))
    f.close()

def ida(states):
    n=int(math.sqrt(len(states)))
    flag=True
    depth=-1
    while(flag):
        depth=depth+1
        path_to_goal=[]
        cost_of_path=0
        nodes_expanded=0
        fringe_size=1
        max_fringe_size=1
        search_depth=0
        max_search_depth=0
        visited=[]
        whole=[states]
        visited_queue=[]
        queue=[{'state':states,'level':0,'action':'root','cost':manhattan(states)}]
        if states==goal:
            flag=False
        while(flag and len(queue)):
            queue = sorted(queue, key=lambda k: k['cost']) 
            nodes_expanded=nodes_expanded+1        
            fringe_size=len(queue)
            if(fringe_size>max_fringe_size):
                max_fringe_size=fringe_size
            current=queue.pop(0)
            visited.append(current['state'])
            visited_queue.append(current)
            index=current['state'].index(0)        
            initial=current['state']
            if initial==goal:
                flag=False
                search_depth=current['level']
                nodes_expanded=nodes_expanded-1
                fringe_size=fringe_size-1
            if(index>n-1):
                swap=index-n
                final=initial[:]
                temp=final[index]
                final[index]=final[swap]
                final[swap]=temp
                if final not in visited and current['level']+1<=depth:
                    if final not in whole:
                        whole.append(final)
                        queue.append({'state':final,'level':current['level']+1,'action':'Up','cost':manhattan(final)+current['level']+1})                
                        if(current['level']+1>max_search_depth):
                            max_search_depth=current['level']+1
                    if final in whole:
                        for item in queue:
                            if item['state']==final:
                                if item['cost']>manhattan(final)+current['level']+1:
                                    queue.remove(item)
                                    queue.append({'state':final,'level':current['level']+1,'action':'Up','cost':manhattan(final)+current['level']+1})
                                    break
                    
            if(index<len(states)-n):            
                swap=index+n
                final=initial[:]
                temp=final[index]
                final[index]=final[swap]
                final[swap]=temp
                if final not in visited and current['level']+1<=depth:
                    if final not in whole:
                        whole.append(final)
                        queue.append({'state':final,'level':current['level']+1,'action':'Down','cost':manhattan(final)+current['level']+1})                
                        if(current['level']+1>max_search_depth):
                            max_search_depth=current['level']+1
                    if final in whole:
                        for item in queue:
                            if item['state']==final:
                                if item['cost']>manhattan(final)+current['level']+1:
                                    queue.remove(item)
                                    queue.append({'state':final,'level':current['level']+1,'action':'Down','cost':manhattan(final)+current['level']+1})
                                    break
            if(index%n!=0):
                swap=index-1
                final=initial[:]
                temp=final[index]
                final[index]=final[swap]
                final[swap]=temp
                if final not in visited and current['level']+1<=depth:
                    if final not in whole:
                        whole.append(final)
                        queue.append({'state':final,'level':current['level']+1,'action':'Left','cost':manhattan(final)+current['level']+1})                
                        if(current['level']+1>max_search_depth):
                            max_search_depth=current['level']+1
                    if final in whole:
                        for item in queue:
                            if item['state']==final:
                                if item['cost']>manhattan(final)+current['level']+1:
                                    queue.remove(item)
                                    queue.append({'state':final,'level':current['level']+1,'action':'Left','cost':manhattan(final)+current['level']+1})
                                    break
            if(index%n!=n-1):
                swap=index+1
                final=initial[:]
                temp=final[index]
                final[index]=final[swap]
                final[swap]=temp
                if final not in visited and current['level']+1<=depth:
                    if final not in whole:
                        whole.append(final)
                        queue.append({'state':final,'level':current['level']+1,'action':'Right','cost':manhattan(final)+current['level']+1})                
                        if(current['level']+1>max_search_depth):
                            max_search_depth=current['level']+1
                    if final in whole:
                        for item in queue:
                            if item['state']==final:
                                if item['cost']>manhattan(final)+current['level']+1:
                                    queue.remove(item)
                                    queue.append({'state':final,'level':current['level']+1,'action':'Right','cost':manhattan(final)+current['level']+1})
                                    break
    current2=visited_queue.pop()
    flag2=True
    while(flag2):
        cost_of_path=cost_of_path+1
        action=current2['action']
        path_to_goal.append(action)
        state=current2['state']
        final2=state[:]
        index2=current2['state'].index(0)
        if(action=='Up'):
            swap=index2+n
            temp=final2[index2]
            final2[index2]=final2[swap]
            final2[swap]=temp
        if(action=='Down'):
            swap=index2-n            
            temp=final2[index2]
            final2[index2]=final2[swap]
            final2[swap]=temp
        if(action=='Left'):
            swap=index2+1            
            temp=final2[index2]
            final2[index2]=final2[swap]
            final2[swap]=temp
        if(action=='Right'):
            swap=index2-1            
            temp=final2[index2]
            final2[index2]=final2[swap]
            final2[swap]=temp
        for x in visited_queue:
            if(x['state']==final2):
                current2=x                
                break
        #current_index = next(index for (index, d) in enumerate(visited_queue) if d['state'] == final)
        #current=visited_queue[current_index]
        if(current2['action']=='root'):
            flag2=False;
    path_to_goal.reverse()
    print ('cost_of_path:',cost_of_path)
    print ('path_to_goal:',path_to_goal)
    print ('nodes_expanded:',nodes_expanded)
    print ('fringe_size:',fringe_size)
    print ('max_fringe_size:',max_fringe_size)
    print ('search_depth:',search_depth)
    print ('max_search_depth:',max_search_depth)
    print ('running_time:',round(time.time() - start_time, 8))
    print('max_ram_usage:',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/float(1024))
    f = open('output.txt','w')
    f.write ('cost_of_path: '+str(cost_of_path)+'\n')
    f.write ('path_to_goal: '+str(path_to_goal)+'\n')
    f.write ('nodes_expanded: '+str(nodes_expanded)+'\n')
    f.write ('fringe_size: '+str(fringe_size)+'\n')
    f.write ('max_fringe_size: '+str(max_fringe_size)+'\n')
    f.write ('search_depth: '+str(search_depth)+'\n')
    f.write ('max_search_depth: '+str(max_search_depth)+'\n')
    f.write ('running_time: '+str(round(time.time() - start_time, 8))+'\n')
    f.write ('max_ram_usage: '+str(round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/float(1024),8)))
    f.close()
    
method=sys.argv[1]
states=list(map(int, sys.argv[2].split(',')))

if method=='bfs':
    bfs(states)
if method=='dfs':
    dfs(states)
if method=='ast':
    ast(states)
if method=='ida':
    ida(states)
