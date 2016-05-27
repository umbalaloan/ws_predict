# views.py 

from django.shortcuts import render, HttpResponse
import requests
from src.model.CandidateMovementModel import CandidateMovementModel
from src.predict.CandidateMovementPrediction import CandidateMovementPrediction
import src.const.TemplateData as templData
import csv
import json
from app.models import UploadFileModel

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def test(request):
    return HttpResponse('My second view!')

def profile(request):
    parsedData = []
    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + username)
        jsonList = []

        jsonList.append(req.json())
        #print jsonList
        userData = {}
        for data in jsonList:
            userData['name'] = data['name']
            userData['blog'] = data['blog']
            userData['email'] = data['email']
            userData['public_gists'] = data['public_gists']
            userData['public_repos'] = data['public_repos']
            userData['avatar_url'] = data['avatar_url']
            userData['followers'] = data['followers']
            userData['following'] = data['following']
        parsedData.append(userData)
    return render(request, 'app/profile.html', {'data': parsedData})
def model(request):
    Data = []
    if request.method=='POST':
        # Create Model
        loc_training_data = 'data/trainingdata/dataset_07_Apr.csv'
        can = CandidateMovementModel(loc_training_data)
        model = can.createCandidateMovementModel()

        test_data = "data/test/sample_test_2.csv"
        file_save= "data/result_prediction.csv"
        predict = CandidateMovementPrediction(model,test_data,file_save)
        data,data_csv = predict.calProbMovementPrediction()
        parsedData=Convert_csv_json(data_csv,'pretty')
        Data_prediction=json.loads(parsedData)
        print Data_prediction
        for data in Data_prediction:
            userData={}
            userData['candidate_id'] = data['candidate_id']
            userData['Employer'] = data['Employer']
            # userData['Moving'] = data['Moving']
            userData['Predicted'] = data['Predicted']
            Data.append(userData)
            # userData['public_repos'] = data['public_repos']
        #     # userData['avatar_url'] = data['avatar_url']
        #     # userData['followers'] = data['followers']
        #     # userData['following'] = data['following']
        print Data
    return render(request, 'app/profile.html', {'data': Data})

def Convert_csv_json(_file_name,format):
        csv_rows=[]
        file_csv=_file_name
        reader=csv.DictReader(file_csv)

        title=reader.fieldnames
        #print title
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        if format=='pretty':
            file_json=json.dumps(csv_rows, sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False)
        else:
            file_json=json.dumps(csv_rows)
        return file_json


def predict(request):
    Data = []
    form = None
    if request.method=='POST':
        # Create Model
        loc_training_data = 'data/trainingdata/dataset_07_Apr.csv'
        can = CandidateMovementModel(loc_training_data)
        model = can.createCandidateMovementModel()
        file = request.FILES['fileUpload']
        file_save= "data/result_prediction.csv"
        predictscore = CandidateMovementPrediction(model,file,file_save)
        # data,data_csv = predictscore.calProbMovementPrediction()
        # parsedData=Convert_csv_json(data_csv,'pretty')
        data, parsedData = predictscore.calProbMovementPrediction()
        Data_prediction=json.loads(parsedData)
        print Data_prediction
        for data in Data_prediction:
            userData={}
            userData['candidate_id'] = data['candidate_id']
            userData['Employer'] = data['Employer']
            # userData['Moving'] = data['Moving']
            userData['Predicted'] = data['Predicted']
            Data.append(userData)
            # userData['public_repos'] = data['public_repos']
        #     # userData['avatar_url'] = data['avatar_url']
        #     # userData['followers'] = data['followers']
        #     # userData['following'] = data['following']
        # print Data
    return render(request, 'app/profile.html', {'data': Data})

def __unicode__(self):
   return unicode(self.some_field) or u''

