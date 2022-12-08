# Subnets
2^# of the subnet bits

# Valid hosts
2^# of hosts bits -2

Valid is -2 because two si occupied by NID and BA



Example

192.168.1.0

Subnet mask
255.255.255.240/28
11111111.11111111.11111111.1111000

Is this a class A, B or C network?
It's a class C by looking at the first octett. 192 is class C. 


2^4 = (2x2x2x2) (the ones in the last octett) = 16 
We can make 4 subnets 

Hosts (the zeros in the last octett)= 
2^4 = 16 -2 = 14   



Ex2

150.150.0.0
255.255.255.252/30
11111111.11111111.11111111.11111100

A, B or C?
Class B. 
150 falls in the range of the class B networks

The first 2 octettes are dedicated to the network portion and will not be changed


Subnets = 2^14 = 16384   
Hosts = 2 ^2 = 4 - 2 = 2 valid hosts 

Creating maaany subnets which all is very small (2)
