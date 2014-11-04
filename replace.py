import csv

#Parses csv input and returns a dict of dicts, i.e. Dict[Router][network]=IP
def parseRouterFile():	
	reader = csv.reader(open('routers.csv'))
	result = {} #dict of dicts, i.e. Dict[Router][network]=IP
	for row in reader:
	    key = row[0]
	    result[key]=[]
	    routerDict={}
	    for item in row[1:]:
	    	if item != '':
	    		splitEntry = item.split()
	    		print splitEntry[0]
	    		network = splitEntry[1].strip('()') #Strip removes chars from the very front and back of string
	    		routerDict[network]=splitEntry[0]
	    result[key].append(routerDict)
	return result




