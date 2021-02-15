
def branches(node,current_level,key,node_store):
    temp_current_level = current_level.copy()
    # print(node_store)

    for index,num in enumerate(node):

        
        
        current_root = temp_current_level[num].copy()
        current_leafnode = current_root[0].get(num).copy()

        # print(current_leafnode)
        if len(current_leafnode) == 1:
            # print(node_store,current_level)
            for k,v in current_level.items():
                for k1,v1 in v[0].items():
                    print(node_store[0],k, *v1)
                    # print(current_level)
                    


                # for keys,values in v:
                #     print(keys,values)
            break
        else:

            
            
            node_store.insert(0,num)
            key=0
            current_level={}
            main(current_leafnode,key,current_level,node_store)

        


        
def main(node,key,current_level,node_store):

    

    #level0

    if key == len(node):
        key=0

        # print("First Level",current_level)

        

        branches(node,current_level,key,node_store)


    else:

        copy_node=node.copy()

        poped=node.pop(key)  #pop root from the array

        # print("Poped",poped)

    
        root_level=[]
        temp=[]


        for i in range(0,len(node)):
            root_level.append(*[node[i]])

            # temp.append(node[i])
        # current_level.update({"root"+str(copy_node[key]):copy_node[key],"leafnodes"+str(copy_node[key]):root_level})
            current_level.update({copy_node[key]:[{copy_node[key]:root_level}]})

            
        main(copy_node,key+1,current_level,node_store)


node=[1,2,3,4]
key=0

current_level={}
node_store=[]
main(node,key,current_level,node_store)
