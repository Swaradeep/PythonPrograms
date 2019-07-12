import java.util.*;
class LexiString{
 public static void main(String args[]){
  char[] order = new char[26];
  char[] a;
  int[] n;
  Scanner s = new Scanner(System.in);
  int cases = s.nextInt();
 while(cases != 0){
  cases--;
  order = s.nextLine();
  a = s.nextLine();
  for(int i = 0; i < a.length; i++){
   for(int j = 0; j < order.length; j++){
    if(a[i] == order[j]){
	n[i] = j;
  }
  }}
  for(int i = 0; i < a.length; i++){
   for(int j = 0; j < order.length; j++){
	if(n[i] > n[j]){
	  int temp = n[i];
	  n[i] = n[j];
	  n[j] = temp;
	  char tem = a[i];
	  a[i] = a[j];
	  a[j] = tem;
   }
  }}
  System.out.println(a);
}
}
}
  