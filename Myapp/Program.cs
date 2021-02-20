using System; 
class FindMissingNumber{
    // Function to ind missing number
    static int getMissingNo(int[] a, int n)
    {
        int total = (n + 1) * (n + 2) / 2;
 
        for (int i = 0; i < n; i++)
            total -= a[i];
 
        return total;
    }
    public static void Main()
    {
        int num;
        Console.WriteLine("Enter the number of inputs:");
        num = Convert.ToInt32(Console.ReadLine());   
        int[] arr = new int[num];
        for(int i=0;i < arr.Length ;i++){
             arr[i] = Convert.ToInt32(Console.ReadLine());
        }
        int miss = getMissingNo(arr, num);
        Console.Write(miss);
    }
}
 