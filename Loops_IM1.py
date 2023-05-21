#!/usr/bin/env python
# coding: utf-8

# # Loops

# 
#     FOR loop
#     While loop
# 

# In[1]:


simple_list=[0,1,2,3,4,5,5,6,88,8,979]
print(simple_list)


# In[2]:


for x in simple_list:
    print(x)


# In[3]:


simple_list[1:5]


# In[5]:


simple_list[5:9]


# In[6]:


for i in simple_list[1:5]:
    for j in simple_list[5:9]:
        print(i*j)


# In[7]:


#looping over a range values
print(range(6))


# In[8]:


for i in range(6):
    print(i)


# In[9]:


#range with starting and end value
for i in range(4,10):
    print(i)


# In[12]:


#range with increment of 2
for i in range(3,25,2):
    print(i)


# In[ ]:





# In[ ]:





# In[3]:


#Printing square from 1 to 10 using a for loop


# In[13]:


x=[1,2,3,4,5,6,7,8,9,10]
for i in x:
    print('Square of {} is {}'.format(i,i*i))


# In[15]:


x=range(11)
for i in x:
    print(f'Square of {i} is {i*i}')


# ### Using IF-ELSE with for Loop

# In[16]:


#Printing squares of even numbers from 1 to 100
x=range(101)
for i in x:
    if i%2==0:     # i mod 2 (i/2 gives a reminder 0 then its a even number)
        print(f'Square of even number {i} is {i*i}')
    


# In[19]:


x=range(101)
for i in x:
    if i%2!=0:     # i mod 2 (i/2 gives a reminder 0 then its a even number)
        print(f'Square of odd number {i} is {i*i}')


# ## While Loop

# In[5]:


#Printing square from 1 to 10
i=5
while i<10:
    print(i)
    i=i+1


# In[3]:


# printing square from 1 to 10 
i=0
while i<=10:
    print(f'Square of {i} is {i*i}')
    i=i+1


# In[1]:


i=0
while i<101:
    if i%2==0:
        print(f'Square of even number {i} is {i*i}')
    i=i+1


# In[3]:


# while loop fro access permission
user_id=input('Enter user name')
password=int(input('Enter password'))
if user_id=='abcd' and password==1234:
    print('Login Success')
else:
    print('Login Failure')


# In[ ]:


user_id=input('Enter user name')
password=int(input('Enter password'))
if user_id=='abcd' and password==1234:
    print('Login Success')
else:
    print('Login Failure')


# In[ ]:





# In[ ]:





# ### Using IF-ELSE with `while` Loop

# In[ ]:


i=0


# In[ ]:





# ## You gotta use your python skills to help your local shopkeeper calculate the Net Price for his shop's product provided below along with it's respective GST slab

# GST Amount = ( Original Cost * GST ) / 100
# 
# Net Price = Original Cost + GST Amount

# Product Cost / GST Slab
# 
# Product1- 1000 / 18%
# 
# Product2- 250 / 18%
# 
# Product3- 125 / 5%
# 
# Product4- 345 / 18%
# 
# Product5- 820 / 12%
# 
# Product6- 980 / 5%
# 
# Product7- 500 / 12%

# In[4]:


# Hint Create a dictionary and loop


# In[4]:


product_gst_slabs={'prooduct1':18,'product2':18,'product3':5,'product4':18,'product5':12,'product6':5,'product7':12}
product_orginal_cost={'prooduct1':1000,'product2':250,'product3':125,'product4':345,'product5':820,'product6':980,'product7':500}


# In[5]:


product_gst_slabs.keys()


# In[9]:


for i in product_gst_slabs.keys():
    gst_amount=(product_orginal_cost[i]+product_gst_slabs[i])/100
    net_price=(product_orginal_cost[i]+gst_amount)
    print('The net price of {} at gst is {}% is {}'.format(i,product_gst_slabs[i],net_price))


# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # User defined functions

# In[ ]:


# # define a function that takes an input, squares it, adds 7, then returns the answer


# In[4]:


def x2p7(x):
    y=x*x
    z=y+7
    return(z)


# In[5]:


x2p7(5)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


# Write a function to add and subtract two variables


# In[6]:


def math_fun(x,y):
    add= x+y
    sub=x-y
    return add, sub


# In[7]:


math_fun(4,7)


# In[8]:


def evenodd(x):
    if x%2==0:
        print('Even Number')
    else:
        print('Odd Number')


# In[11]:


evenodd(109)


# In[ ]:





# In[ ]:





# In[ ]:





# In[6]:


### Write a UDF that returns true if the input is a prime number and False otherwise.


# In[14]:


def prime(n):
    if (n==1):
        return False
    elif(n==2):
        return True
    else:
        for x in range(2,n):
            if(n%x==0):
                return False
    return True


# In[16]:


prime(20)


# In[ ]:





# In[7]:


### Write a UDF that takes a list as input and returns the reverse list.


# In[18]:


def Reversing(listing):
    listing.reverse()
    return lst


# In[19]:


lst=[45,87,12,8,657]


# In[20]:


Reversing(lst)


# In[24]:


# Lamda function


# In[25]:


lam1=lambda x: x*x+8
print(lam1(7))


# In[26]:


lam2=lambda x,y,z: x*y+y*z+y/z
print(lam2(5,7,9))


# In[27]:


lam2(8,4,1)


# In[28]:


lam1(66)


# In[ ]:




