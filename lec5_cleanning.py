mail=input("Enter your mail ")
loc1=mail.find("@")
loc2=mail.find(".",loc1)#start searching from the location of @ to avoid the case which has "." in the user name
vendor=mail[loc1+1:loc2]
print(vendor)
