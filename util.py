import json
import pickle
import numpy as np
data_columns=None
model=None
#['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']

sex_options=None
chestpaintype_options=None
restingecg_options=None
exerciseangina_options=None
stslope_options=None

def load_artifacts():
    print('Loading artifacts start...')
    global data_columns
    global model
    global sex_options
    global chestpaintype_options
    global restingecg_options
    global exerciseangina_options
    global stslope_options
    with open(r"columns.json","r") as f:
       data_columns=json.load(f)["data_columns"]
       sex_options=data_columns[6:8]
       chestpaintype_options=data_columns[8:12]
       restingecg_options=data_columns[12:15]
       exerciseangina_options=data_columns[15:17]
       stslope_options=data_columns[17:20]
    with open(r'clf.pkl','rb') as f:
      model=pickle.load(f)
    print("loading artifacts done...")
    
def get_sex_names():
   return sex_options
def get_chestpaintype_names():
   return chestpaintype_options
def get_restingecg_names():
   return restingecg_options
def get_exerciseangina_names():
   return exerciseangina_options
def get_stslope_names():
   return stslope_options
def is_heartdisease(Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope):
   sex_index=data_columns.index(Sex[0])
   chestpaintype_index=data_columns.index(ChestPainType[0])
   restingecg_index=data_columns.index(RestingECG[0])
   exerciseangina_index=data_columns.index(ExerciseAngina[0])
   stslope_index=data_columns.index(ST_Slope)
   x=np.zeros(len(data_columns))
   x[0]=Age[0]
   print(Age[0])
   x[1]=RestingBP[0]
   x[2]=Cholesterol[0]
   x[3]=FastingBS[0]
   x[4]=MaxHR[0]
   x[5]=Oldpeak[0]
   if sex_index>=0:
      x[sex_index]=1
   if chestpaintype_index>=0:
      x[chestpaintype_index]=1
   if restingecg_index>=0:
      x[restingecg_index]=1
   if exerciseangina_index>=0:
      x[exerciseangina_index]=1
   if stslope_index>=0:
      x[stslope_index]=1
   return model.predict([x])[0]

if __name__=='__main__':
   load_artifacts()
   print(is_heartdisease( 40	,'M'	,'ATA',140,	289,	0,	'Normal',	172,	'N',	0.0,	'Up'))


