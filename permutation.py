
def branches(node,current_level,key):
    temp_current_level = current_level.copy()

    for index,num in enumerate(node):
        
        current_root = temp_current_level["root"+str(num)].copy()

        current_leafnode = current_root[0].get("leafnodes"+str(num)).copy()

        # print(current_leafnode)

        if len(current_leafnode) == 1:
            print("Recursion2",current_level)

        else:

            key=0

            print(*current_leafnode)

            current_level={}
            main(current_leafnode,key,current_level)

        


        
def main(node,key,current_level):

    

    #level0

    if key == len(node):

        key=0

        print("Recurrsion1",current_level)

        branches(node,current_level,key)


    else:

        copy_node=node.copy()

        node.pop(key)  #pop root from the array

    
        root_level=[]
        temp=[]


        for i in range(0,len(node)):
            root_level.append(*[node[i]])

            # temp.append(node[i])
        # current_level.update({"root"+str(copy_node[key]):copy_node[key],"leafnodes"+str(copy_node[key]):root_level})
            current_level.update({"root"+str(copy_node[key]):[{"leafnodes"+str(copy_node[key]):root_level}]})


        # print(copy_node[key],*root_level)

        # print(current_level)

        # print(*temp)

        main(copy_node,key+1,current_level)



    #Now print for all the keys breadth wise



node=[1,2,3]
key=0

current_level={}
main(node,key,current_level)
