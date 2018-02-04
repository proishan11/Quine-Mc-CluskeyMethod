def decimalToBinary(minterms_decimal, variables):
    result = []
    temp = ""
    for i in minterms_decimal:
        for j in range(variables):
            if(i%2 == 0):
                temp = "0"+temp
            else:
                temp = "1"+temp
            i = i//2
        result.append(temp)
        temp = ""
    return result

def orderMinterms(mintems_binary, no_of_var, no_of_minterms, minterms_decimal):
    result = {}
    for i in range(no_of_var+1):
        result[i] = []
    for i in range(no_of_minterms):
        data = mintems_binary[i]
        temp_list = []
        temp = data.count("1")
        temp_list.append(data)
        
        temp_list.append(0)
        
        temp_list.append(minterms_decimal[i])
        result[temp].append(temp_list)
        
    return result

#Check if given two string differ at only a single index
def isGroupable(a, b):
    count = 0
    for i in range(len(a)):
        if(a[i] != b[i]):
            count+=1
    return(count==1)

#Replace the uncommon index with '-'
def combine(a, b):
    combined = ""
    for i in range(len(a)):
        if(a[i]!=b[i]):
            combined+='-'
        else:
            combined+=a[i]
    return combined
    
#group min terms and store result in whole_data
def groupMinterms(minterms_ordered,number,whole_data):
    new_data = {}
    flag = 0
    for i in range(number+1):
        new_data[i] = []
    for i in range(number):
        for j in minterms_ordered[i]:
            if(j!=[]):
                for k in minterms_ordered[i+1]:
                    if(k!=[]):
                        if(isGroupable(j[0],k[0])):
                            flag = 1
                            combined = combine(j[0],k[0])
                            j[1] = 1
                            k[1] = 1
                            index = combined.count("1")
                            temp_list = []
                            temp_list.append(combined)
                            temp_list.append(0)
                            for x in range(2,len(j)):
                                temp_list.append(j[x])
                            for x in range(2, len(k)):
                                if(k[x] not in temp_list):
                                    temp_list.append(k[x])
                            new_data[index].append(temp_list)
    if(flag == 0):
        return
    else:
        whole_data.append(minterms_ordered)
        if(new_data not in whole_data):
            whole_data.append(new_data)    
        groupMinterms(new_data,number,whole_data)
    return whole_data

def getAllSelected(POS,temp,allSelected,index):
	if index==len(POS):
		temp1=temp+[]
		allSelected.append(temp1)
		return
	else:
		for i in POS[index]:
			if i not in temp:
				temp.append(i)
				getAllSelected(POS,temp,allSelected,index+1)
				temp.remove(i)
			else:
				getAllSelected(POS,temp,allSelected,index+1)

def counter(list):
	count =0
	for string in [x[0] for x in list]:
		for i in string:
			if i=='0' or i=='1':
				count+=1

	return count

def get_minimal_implicants(selected_primeImplicants):
	minimal_implicants=[]
	minimum=999999
	for i in selected_primeImplicants:
		if counter(i)<minimum:
			minimum=counter(i)

	for i in selected_primeImplicants:
		if counter(i)==minimum:
			minimal_implicants.append(i)

	return minimal_implicants

def petrick_selection(feed,selected_primeImplicants):
    temp_list = []
    pos = []
    allSelected = []
    for i in feed:
        pos.append(feed[i])
    getAllSelected(pos,temp_list,allSelected,0)
    for i in allSelected:
        if len(i)==min([len(x) for x in allSelected]):
            if i not in selected_primeImplicants:
                selected_primeImplicants.append(i)
    return selected_primeImplicants

def printImplicants(implicants, parameter):
	for string in implicants:
		count=-1
		for i in string:
			count+=1
			if i=='0':
				print(chr(ord('a')+count)+"'",end="")
			elif i =='1':
				print(chr(ord('a')+count),end="")
		print("  " + parameter+ "  ",end="")
    
def tabulation(no_of_var=0, no_of_minterms=0, minterms_decimal=[]):
    whole_data = {}
    primeImplicants = []
    essentialPrimeImplicants = []
    whole_data = []
    mapping = {}
    selected_primeImplicants = []
    binary_primeImplicants = []
    mintems_binary = decimalToBinary(minterms_decimal, no_of_var)
    minterms_ordered = orderMinterms(mintems_binary, no_of_var, no_of_minterms, minterms_decimal)
    whole_data = groupMinterms(minterms_ordered,no_of_var,whole_data)
    for i in whole_data:
        for j in i:
            for k in i[j]:
                if(i[j]==[]):
                    break
                temp_count = 0
                if(k not in primeImplicants and k[1]==0):
                        for l in primeImplicants:
                            if(k[0] == l[0]):
                                temp_count = 1
                        if(temp_count==0):
                            primeImplicants.append(k)
    
    for i in minterms_decimal:
        mapping[i] = []
    for i in primeImplicants:
        for j in range(2,len(i)):
            mapping[i[j]].append(i[0])
    
    for i in mapping:
        if(len(mapping[i]) == 1):
            if(mapping[i][0] not in essentialPrimeImplicants):
                essentialPrimeImplicants.append(mapping[i][0])

    feed = mapping
    del_list = []
    for i in essentialPrimeImplicants:
        for j in primeImplicants:
            if(j[0] == i):
                for k in range(2,len(j)):
                    if(j[k] not in del_list):
                        del_list.append(j[k])
    
    for i in del_list:
        del feed[i]
    
    selected_primeImplicants =  petrick_selection(feed, selected_primeImplicants)
    minimal_primeImpicants = get_minimal_implicants(selected_primeImplicants)
    
    for i in primeImplicants:
        binary_primeImplicants.append(i[0])
    
    finalFunction = []
    for i in minimal_primeImpicants:
        finalFunction.append(essentialPrimeImplicants+i)
    return finalFunction[0]   
    
if __name__ == '__main__':
    tabulation()
