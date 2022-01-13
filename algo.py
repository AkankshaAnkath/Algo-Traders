
import pandas as pd

def algo(amount,tenure,risk_factor):
    df_original=pd.read_csv('Data.csv')

    df=df_original.copy(True)

    last_date = df.columns[-1]


    ##case 1 amount condn satisfied

    for i in range(0,len(df)):
        if(amount<float(df.loc[i,str(last_date)])):
            df=df.drop(i)
    df.reset_index(drop=True,inplace=True)


    ## case2 taking average and rf
    

    per_list=[]
    rf_list=[]

    for i in range(0,len(df)):

        percentage_total=0
        rf=0
        nos=0
        for j in range(1,(len(df.columns)-tenure)):
            next_tenure_data=df.iloc[i,(j+tenure)]
            current_tenure_data=df.iloc[i,j]

            if(current_tenure_data!=0):
                percentage=(((next_tenure_data)-(current_tenure_data))/(current_tenure_data))*100

                percentage_total+=percentage
                
                
               
                nos+=1
            
                if(percentage<0):
                    rf=max(rf,-percentage)

            
                
        percentage_total/=nos

        per_list.append(percentage_total)
        rf_list.append(rf)
        
    
    df["Percentage"]=per_list 
    df["rf"]=rf_list
    df.fillna(0)
    
    
    ####STEP 3#####
    ##Sorting####
    
    #Checks if RF Condition is satisfied
    for i in range(0,len(df)):
        if(risk_factor<df.loc[i,"rf"]):
            df=df.drop(i)
    df.reset_index(drop=True,inplace=True)
    
    #SORT PERCENTAGE IN DESCENDING ORDER
    df=df.sort_values(["Percentage","rf"],ascending=[False,True])
    df.reset_index(drop=True,inplace=True)
   

    
    return df


# print(algo(10000,2,30))

     
    

