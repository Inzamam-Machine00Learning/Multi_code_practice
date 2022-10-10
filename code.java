//Hello World
class Main {
  public static void main(String[] args) {
    System.out.println("Hello world!");
  }
}

// This is a single line comment
/* This is a multi-line comment.
You can keep multiple lines as 
comment in this area.*/

// The main Method
/*
Any code inside the main() method will be executed. Don't worry about the keywords before and after main. You will get to know them bit by bit while reading this tutorial.

For now, just remember that every Java program has a class name which must match the filename, and that every program must contain the main() method.
System.out.println()
Inside the main() method, we can use the println() method to print a line of text.
public static void main(String[] args) {
  System.out.println("Hello World");
}
Print Text
println() method to output values or print text in Java
System.out.println("Hello World!");

System.out.println("Hello World!");
System.out.println("I am learning Java.");
System.out.println("It is awesome!");

Double Quotes
When you are working with text, it must be wrapped inside double quotations marks "".
If you forget the double quotes, an error occurs
System.out.println(This sentence will produce an error);
*/
//The Print() Method
//There is also a print() method, which is similar to println()
public class Main {
  public static void main(String[] args) {
    System.out.print("Hello World! ");
    System.out.print("I will print on the same line.");
  }
}
