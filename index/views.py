from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
resume = [
    {'group' : 'Education','title' : 'Schooling', 'Info' :{'name' : 'Little Flower EM School','loc':'Guntur, AP, India', 'board' : 'ICSE', 'Passedout': 2015, 'Percentage/CGPA' : '80%' }   , 'image' : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2OeI-UTM4oFZMbYwydb-mvMv8SCXSMMUUnhGh2S_NovXT4QOpKsRTgqeu6AZNPwaWv4Y&usqp=CAU"},
    {'group' : 'Education','title' : '12 / Intermediate', 'Info' :{'name' : 'Sri Chaitannya jr','loc':'Guntur, AP, India', 'board' : 'BIEAP', 'Passedout': 2017, 'Percentage' : '93%' }   , 'image' : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2OeI-UTM4oFZMbYwydb-mvMv8SCXSMMUUnhGh2S_NovXT4QOpKsRTgqeu6AZNPwaWv4Y&usqp=CAU"},
    {'group' : 'Education','title' : 'Engineering / B.Tech', 'Info' :{'name' : 'KHIT','loc':'Guntur, AP, India', 'board' : 'JNTUK', 'Passedout': 2021, 'Percentage' : 7.3}   , 'image' : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2OeI-UTM4oFZMbYwydb-mvMv8SCXSMMUUnhGh2S_NovXT4QOpKsRTgqeu6AZNPwaWv4Y&usqp=CAU"},
    {'group' : 'Experience','title' : 'Experience', 'Info' :{'name' : 'Infosys','tech':'SAP ABAP (ABAP developer)', 'period' : '1.6 yrs(Joined 2021,Aug)', 'dev': 'Worked on many Developments of ABAP elements.such as Dictionaries, Report programs, new Tcodes, Smart forms, Scripts, FM, BAPIs, Custom BADI implementation, Custom Enhancements etc. And have Vast experience on Debugging issues'}   , 'image' : "https://uploads-ssl.webflow.com/5a9ee6416e90d20001b20038/62ee027b0c783a2ca5cbc0e5_Rectangle%201%20(38).svg"},
    {'group' : 'Skills','title' : 'Skills', 'Info' :{'web' : 'HTML, CSS, JS','webf':'Django', 'lang' : 'Python, C++, MYSQL, ABAP', 'ot': 'SAP'}   , 'image' : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpA7eG8D17J9sKlmIMf58j1XNOLuLfiYV7jMhTXijfW_dC7r0WocCoxhN0l671Q-ZnS6E&usqp=CAU"},
    {'group' : 'Certification','title' : 'Certification', 'Info' : {1:'Certification in developing a complete website using HTML, CSS, JS, PHP, and MySQL as a database. From Internshala', 2 : 'Infosys Foundation Program- SAP ABAP (Infosys certified ABAP developer)'}   , 'image' : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLcKEBokzhSeSt-Zg88uQVkahyjMM2qEeZQLl9UPb4gY2ADQq0HTxhsrnPy50uSPunr7o&usqp=CAU"},
    {'group' : 'Intrst','title' : 'Interests / Hobbies', 'Info' :{'interests' : 'Learning New/Unknown stuff, Playing / Watching Cricket, Dancing when alone, Ofcourse #MUSIC is stressbuster, Watching Movies/Series(BingeWatcher)'}, 'image' : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQE5ENIxFwJ6_jAGPUaS1BgtbVwuc0z-_AD6nSxnhMXCEVvMGRL2jjHOi00r2FPtXHlLbI&usqp=CAU"},
]

def index(request):
    return render(request, "index/index.html", {
        "title" : 'MSP',
        'resume' : resume,
    })

