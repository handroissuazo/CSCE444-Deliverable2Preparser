import json
import csv

with open("Leso.csv","r") as f:
	lesoReader = csv.reader(f)
	keys =(next(lesoReader))
	equipTypesA = []
	equipTypesB = []
	equipTypesC = []
	equipTypesD = []
	equipTypesE = []
	equipTypesF = []
	equipTypesQ = []
	equipTypesP = []
	lesoSummary = {}

	for row in lesoReader:
		if(row[0] in lesoSummary):
			if( row[7] in lesoSummary[row[0]] ):
				lesoSummary[row[0]][row[7]] += 1
			else:
				lesoSummary[row[0]][row[7]] = 1
		else:
			lesoSummary[row[0]] = {row[7] : 1}

		emptyRow = dict.fromkeys(keys, "")
		emptyRow["State"] = row[0]
		emptyRow["Station Name (LEA)"] = row[1]
		emptyRow["NSN"] = row[2]
		emptyRow["Item Name"] = row[3]
		emptyRow["Quantity"] = row[4]
		emptyRow["UI"] = row[5]
		emptyRow["Acquisition Value"] = row[6]
		emptyRow["DEMIL Code"] = row[7]
		emptyRow["DEMIL IC"] = row[8]
		emptyRow["Ship Date"] = row[9]
		emptyRow["PSC NAME"] = row[10]

		if(emptyRow["DEMIL Code"] == "A"):
			equipTypesA.append(emptyRow)
		elif(emptyRow["DEMIL Code"] == "B"):
			equipTypesB.append(emptyRow)
		elif(emptyRow["DEMIL Code"] == "C"):
			equipTypesC.append(emptyRow)
		elif(emptyRow["DEMIL Code"] == "D"):
			equipTypesD.append(emptyRow)
		elif(emptyRow["DEMIL Code"] == "E"):
			equipTypesE.append(emptyRow)
		elif(emptyRow["DEMIL Code"] == "F"):
			equipTypesF.append(emptyRow)
		elif(emptyRow["DEMIL Code"] == "P"):
			equipTypesQ.append(emptyRow)
		elif(emptyRow["DEMIL Code"] == "Q"):
			equipTypesP.append(emptyRow)


with open("lesoA.json", "w+") as f:
	json.dump(equipTypesA, f)
with open("lesoB.json", "w+") as f:
	json.dump(equipTypesB, f)
with open("lesoC.json", "w+") as f:
	json.dump(equipTypesC, f)
with open("lesoD.json", "w+") as f:
	json.dump(equipTypesD, f)
with open("lesoE.json", "w+") as f:
	json.dump(equipTypesE, f)
with open("lesoF.json", "w+") as f:
	json.dump(equipTypesF, f)
with open("lesoP.json", "w+") as f:
	json.dump(equipTypesQ, f)
with open("lesoQ.json", "w+") as f:
	json.dump(equipTypesP, f)

with open("lesoSummary.json", "w+") as f:
	json.dump(lesoSummary, f, indent=4)
