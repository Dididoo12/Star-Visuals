/*

Author: Edward Tang
Date: September 6, 2018
Purpose: This program is designed to determine the digit sum (a single-digit sum of the digits in a given number) of a number.

*/

// The "Diamonds" class.
import java.awt.*;
import hsa.Console;

public class Diamonds
{
    static Console c;           // The output console

    public static void main (String[] args)
    {
	c = new Console (30,80, "Diamonds");
	String restart;
	
	do
	{
	    
	    int shape = readBoundInt (1,2,"Enter the type of shape (1 for diamond, 2 for hourglass): ","[INVALID INPUT] Enter 1 for diamond, 2 for hourglass: ");
	    c.println();
	    int fill = readBoundInt (1,2,"Enter the type of fill (1 for filled, 2 for hollow): ","[INVALID INPUT] Enter 1 for filled, 2 for hollow: ");
	    c.println();

	    int size;
	    int stars;
	    int spaces = 0;
	    
	    if (shape == 1)
	    {
		size = readBoundInt (1,25,"Enter the size of the shape (odd integer from 1-25): ","[INVALID INPUT] You must enter an odd integer from 1-25): ",1);
		c.println ();
		c.println ("size = " + size);
		stars = size;
		
		if (fill == 1)
		{
		    c.print (" ");
		    spaces = 1;
		    do
		    {
			for (int i = 1 ; i <= stars ; i++)
			    c.print ("*");
			stars += 2;
			c.println();
		    }
		    while (stars <= size + 2);
	    
		    stars = size;
	    
		    do
		    {
			for (int i = 1 ; i <= spaces ; i++)
			    c.print(" ");
			for (int i = 1 ; i <= stars ; i++)
			    c.print ("*");
			    
			stars -= 2;
			spaces += 1;
			c.println();
		    }
		    while (stars > 0);
		}
		else
		{
		    c.print (" ");
		    int infill = size;
		    
		    for (int i = 1 ; i <= stars ; i++)
			c.print ("*");
		    c.println();
		    do
		    {
			for (int i = 1 ; i <= spaces ; i++)
			    c.print (" ");
			c.print ("*");
			for (int i = 1 ; i <= infill ; i++)
			    c.print (" ");
			c.print ("*");
			c.println();
			
			infill -= 2;
			spaces += 1;
		    }
		    while (infill > -1);
		    for (int i = 1 ; i <= spaces ; i++)
			c.print (" ");
		    c.print("*");
		    c.println();
		}
	    }
	    else
	    {
		size = readBoundInt (5,25,"Enter the size of the shape (odd integer from 5-25): ","[INVALID INPUT] You must enter an odd integer from 5-25): ",1);
		c.println ();
		c.println ("size = " + size);
		stars = size;
		
		if (fill == 1)
		{
		    do
		    {
			for (int i = 1 ; i <= spaces ; i++)
			    c.print(" ");
			for (int i = 1 ; i <= stars ; i++)
			    c.print ("*");
			stars -= 2;
			spaces += 1;
			c.println();
		    }
		    while (stars > 3);
		
		    do
		    {
			for (int i = 1 ; i <= spaces ; i++)
			    c.print(" ");
			for (int i = 1 ; i <= stars ; i++)
			    c.print ("*");
			stars += 2;
			spaces -= 1;
			c.println();
		    }
		    while (stars <= size);
		}
		else
		{
		    spaces = 1;
		    int infill = size - 4;
		    for (int i = 1 ; i <= stars ; i++)
			c.print ("*"); 
		    c.println();
		    while (infill > 1)
		    {
			for (int i = 1 ; i <= spaces ; i++)
			    c.print(" ");
			c.print("*");
			for (int i = 1 ; i <= infill ; i++)
			    c.print (" ");
			c.print("*");
			infill -= 2;
			spaces += 1;
			c.println();
		    }
		
		    do
		    {
			for (int i = 1 ; i <= spaces ; i++)
			    c.print(" ");
			c.print("*");
			for (int i = 1 ; i <= infill ; i++)
			    c.print (" ");
			c.print("*");
			infill += 2;
			spaces -= 1;
			c.println();
		    }
		    while (infill <= size - 4);  
		    for (int i = 1 ; i <= stars ; i++)
			c.print ("*");
		    c.println();
		}
	    }

	    c.println ();
	    c.print ("Enter anything to choose another shape, or enter 'stop' to stop the program: ");
	    c.println ();
	    restart = c.readString ();
	    c.println ();
	}
	while (!restart.equals ("stop"));
	
	// Place your program here.  'c' is the output console
    } // main method
    
    /*

    Author: Edward Tang
    Date: September 7, 2018
    Purpose: This method is designed to request input from the user for an integer value, redo the input request with an error message if the value is not within desired bounds 
	     (inclusive range, [OPTIONAL] odd/even), and return a "valid" input.
    Input: [int] The minimum integer value, [int] the maximum integer value, [String] the desired input request message, [String] the desired error message, [int] desired integer 
	   parity (DEFAULT impossible parity, AKA no eventual parity check)
    Output: [int] An integer within the desired range, inclusively

    */      
    
    public static int readBoundInt (int intMin, int intMax, String readRequest, String error, int parity)
    {
	c.print(readRequest);
	int num = c.readInt();
	while (num < intMin || num > intMax || (num % 2 == 0 && parity == 1) || (num % 2 != 0 && parity == 0))
	{
	    c.print(error);
	    num = c.readInt();
	}
	return num;
    }
    
    public static int readBoundInt (int intMin, int intMax, String readRequest, String error)
    {    
	 return readBoundInt(intMin, intMax, readRequest, error, 3);
    }
} // Diamonds class


