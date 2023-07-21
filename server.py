from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import util
import uvicorn
app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates=Jinja2Templates(directory='templates')
# "Age", "Sex", "ChestPainType", "RestingBP", "Cholesterol", "FastingBS", "RestingECG", "MaxHR", "ExerciseAngina", "Oldpeak", "ST_Slope"]
@app.get('/home',response_class=HTMLResponse)
def home(request:Request):
    return templates.TemplateResponse("app.html",context={'request':request})
@app.post('/is_heart_disease',response_class=HTMLResponse)
async def is_heart_disease(request:Request,response_class=HTMLResponse):
    form_data=await request.form()
    Age=float(form_data.get('Age')),
    Sex=form_data.get('Sex'),
    ChestPainType=form_data.get('ChestPainType'),
    RestingBP=float(form_data.get('RestingBP')),
    Cholesterol=float(form_data.get('Cholesterol')),
    FastingBS=float(form_data.get('FastingBS')),
    RestingECG=form_data.get('RestingECG'),
    MaxHR=float(form_data.get('MaxHR')),
    ExerciseAngina=form_data.get('ExerciseAngina'),
    Oldpeak=float(form_data.get('Oldpeak')),
    ST_Slope=form_data.get('ST_Slope')
    
    result=util.is_heartdisease(Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope)
    
    return templates.TemplateResponse("app.html",context={'request':request,"result":result})
    
    

if __name__=='__main__':
    util.load_artifacts()
    uvicorn.run(app)


    








