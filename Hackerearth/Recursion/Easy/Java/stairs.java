
import java.util.*;


class TestClass {

    public static int recur(int num)
    {
        if(num == 1 || num == 2)
        {
            return num;
        }
        else if(num == 3)
        {
            return 4;
        }
        else
        {
            return recur(num-1)+recur(num-2)+recur(num-3);
        }
    }

    public static void main(String args[] ) throws Exception {
   
        //Scanner
        Scanner sc=new Scanner(System.in);
        int num=sc.nextInt();               
        int result= recur(num);
        System.out.println(result);

    }

}
