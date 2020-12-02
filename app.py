from flask import Flask, request, render_template
from math import sqrt
import pandas as pd
import numpy as np
from shutil import copyfile

app = Flask(__name__)

def spec(df,benchmark,client):
    df2=df.copy()
    df2=df2[df2["benchmark"] == benchmark]
    df2.sort_values(by='SPEC_ratio', ascending=False, inplace=True, ignore_index=True)
    rank=str(list(df2["client_id"]).index(client)+1)
    return rank
    

@app.route('/benchmarks' ,methods=['POST'])
def ev():
	
	df = pd.read_csv("records.csv")
	sent_json = request.get_json(force=True)

	prd=1
	SPECS=[]
	index_reference=df[df["client_id"] == 1].index[0]
	
	if sent_json["hostname"] not in df["client_hostname"].values:
		c=df["client_id"].max()+1
		counter=0
		for i in sent_json["benchmarks"]:
			df.loc[df.index.max()+1]=[c,sent_json["hostname"],i["name"],i["score"],float(df.loc[index_reference+counter,"Execution time"])/float(i["score"]), -9999]
			SPECS.append(float(df.loc[index_reference+counter,"Execution time"])/float(i["score"]))
			counter+=1
	else:
		c = df[df["client_hostname"] == sent_json["hostname"]].iloc[0]["client_id"]
		df.drop(df[df["client_hostname"] == sent_json["hostname"]].index, inplace=True)
		df.reset_index(drop=True,inplace=True)
		index_reference=df[df["client_id"] == 1].index[0]
		counter=0
		for i in sent_json["benchmarks"]:
			df.loc[df.index.max()+1]=[c,sent_json["hostname"],i["name"],i["score"],float(df.loc[index_reference+counter,"Execution time"])/float(i["score"]), -9999]
			SPECS.append(float(df.loc[index_reference+counter,"Execution time"])/float(i["score"]))
			counter+=1

	SPECS=sqrt(np.array(SPECS).prod())
	df["Geometric mean"].replace({-9999:SPECS}, inplace=True)
	df.sort_values(by='Geometric mean', ascending=False, inplace=True, ignore_index=True)
	df.to_csv("records.csv", index=False, encoding="utf-8")
	ranking=list(df["client_id"].unique()).index(c)+1
	copyfile("records.csv","./static/db.csv")
	statement1 = "your rank for CPU  is: "+spec(df,"bubbleSort",c)+" \n"
	statement2 = "your rank for STORAGE  is: "+spec(df,"fileEdit",c)+" \n"
	statement3 = "your rank for RAM  is: "+spec(df,"binaryTree",c)+" \n"
	statement4 = "your rank for MEMORY  is: "+spec(df,"hanoi",c)+" \n"
	statement5 = "your rank for WIFI CARD  is: "+spec(df,"network",c)+" \n"
	return "Your benchmark result is: " + str(SPECS) + " with a ranking of: " + str(ranking) + "/" + str((df.index.max()+1)//5) + "\n \n" +statement1+statement2+statement3+statement4+statement5

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/db')
def db():
    return render_template("download.html")

if __name__ == '__main__':
	app.run(debug = True)
