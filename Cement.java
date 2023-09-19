import java.util.*;

public class Cement{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    String name;
    String address;
    double width;
    double length;
    double installationFee = 1200;
    // all pools have an outer 4 corners
    // each corner is 6x6 ft and half a foot deep
    double cost = 4 * 6 * 6 * 0.5;
    // converts cost from cubic feet to yards
    cost /= 27;
    // gets the cost of the 4 corners of concrete
    cost *= 419.95;
    // taxes
    //cost *= 1.055;

    //prompts user for name
    System.out.println("What is your name?");
    name = input.nextLine();

    //promts user for address
    System.out.println("What is your address?");
    address = input.nextLine();

    // prompts user for pool width
    System.out.println("What is the width of the pool?");
    width = input.nextInt();

    // prompts user for pool length
    System.out.println("What is the length of the pool?");
    length = input.nextInt();

    
    // initializes cement as the pool perimeter
    double cement = (length + width) * 2;
    // gets the area of cement needed in square feet
    cement *= 6;
    // makes the cement 6 inches deep (half a foot)
    cement *= 0.5;
    // converts cement from cubic feet to cubic yards
    cement /= 27;
    // gets raw cost of cement
    cement *= 419.95;
    // gets tax of cement
    cost += cement;
    double cementTax = (cost * 1.055) - cost;

    System.out.println("Name: " + name);
    System.out.println("Address: " + address);
    System.out.printf("Installation Fee: $%,.2f%n", installationFee);
    System.out.printf("Cement Cost @ $419.95/cubic yard: $%,.2f%n", cost);
    System.out.printf("Tax: $%,.2f%n", cementTax);
    System.out.printf("Total: $%,.2f%n", (cost + installationFee + cementTax));
    
  }
}