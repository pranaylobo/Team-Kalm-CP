def solve(n):
    
    if n==0 or n==1:
        return 1

    elif n==2:
        return 2

    elif n==3:
        return 4

    elif n==4:
        return 7

    elif n==5:
        return 13

    elif n==6:
        return 24

    elif n==7:
        return 44


    else:
        return solve(n-1) + solve(n-2) + solve(n-3)




print(solve(int(input())))