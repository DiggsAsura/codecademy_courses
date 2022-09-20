### Article only
# Basic Data Types

int        integer numbers           0, 420 
double     floating-point numbers    3.14, -300.03
char       characters                'a', 'b'
string     sequence of characters    "Hello World!"
bool       truth values              true, false


int age = 28;
double price = 8.99;
char grade = 'A';
std::string message = "Game on";
bool late_to_work = true;


Data type modifiers in C++ are:
- signed
- unsigned
- short
- long


### Const:

const (constant) variables cannot be changed by your program during execution.

const double quarter = 0.25;

// and now variable quarter can only be 0.25


### Type Conversion:

A type cast is basically a conversion from one type to another.

The notation (type) value means "convert value to type". So for example:

double weight1;
int weight2;

weight1 = 154.49;
weight2 = (int) weight1;

// weight2 is now 154 

**Note**: Going from a double to an int simply removes the decimal. There is no rounding. 
