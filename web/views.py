from os import error
from django.shortcuts import render
from matplotlib import pyplot as plt
from numpy import empty
import pandas as pd
import matplotlib as mpl
from django.core.files.storage import FileSystemStorage

           
def home(request):
    context = {}
    if request.method == 'POST': 
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()    
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
            context['df'] = df
            context['head'] = df.head(10)
            if request.POST.get('column1') == '' or request.POST.get('column1') not in df.columns:
                column1 = df.columns[0]
            else:
                column1 = request.POST.get('column1')
            if request.POST.get('column2') == '' or request.POST.get('column2') not in df.columns:
                column2 = df.columns[1]
            else:
                column2 = request.POST.get('column2')
            graph_type = request.POST.get('graphtype')
            if request.POST.get('xlabel') == '':
                xlabel = ''
            else:
                xlabel = request.POST.get('xlabel')
            if request.POST.get('ylabel') == '':
                ylabel = ''
            else:
                ylabel = request.POST.get('ylabel')
            if request.POST.get('titlename') == '':
                title_name = ''
            else:
                title_name = request.POST.get('titlename')
            if graph_type == 'bar' or graph_type == 'Bar':
                context['plot'] = df.plot(kind='bar', x=column1, y=column2, figsize=(10, 5))
                context['plot']=plt.title(title_name)
                context['plot']=plt.xlabel(xlabel)
                context['plot']=plt.ylabel(ylabel)
                context['plot'].get_figure().savefig('media/plot.png')
                context['plot_url'] = 'media/plot.png'
            elif graph_type == 'line' or graph_type == 'Line':
                context['plot'] = df.plot(kind='line', x=column1, y=column2, figsize=(10, 5))
                context['plot']=plt.title(title_name)
                context['plot']=plt.xlabel(xlabel)
                context['plot']=plt.ylabel(ylabel)
                context['plot'].get_figure().savefig('media/plot.png')
                context['plot_url'] = 'media/plot.png'
            elif graph_type == 'scatter' or graph_type == 'Scatter':
                context['plot'] = df.plot(kind='scatter', x=column1, y=column2, figsize=(10, 5))
                context['plot']=plt.title(title_name)
                context['plot']=plt.xlabel(xlabel)
                context['plot']=plt.ylabel(ylabel)
                context['plot'].get_figure().savefig('media/plot.png')
                context['plot_url'] = 'media/plot.png'
            elif graph_type == 'hist' or graph_type == 'Hist':
                context['plot'] = df.plot(kind='hist', x=column1, y=column2, figsize=(10, 5))
                context['plot']=plt.title(title_name)
                context['plot']=plt.xlabel(xlabel)
                context['plot']=plt.ylabel(ylabel)
                context['plot'].get_figure().savefig('media/plot.png')
                context['plot_url'] = 'media/plot.png'
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
            context['df'] = df
            context['head'] = df.head(10)
            if request.POST.get('column1') == '' or request.POST.get('column1') not in df.columns:
                column1 = df.columns[0]
            else:
                column1 = request.POST.get('column1')
            if request.POST.get('column2') == '' or request.POST.get('column2') not in df.columns:
                column2 = df.columns[1]
            else:
                column2 = request.POST.get('column2')
            graph_type = request.POST.get('graphtype')
            if request.POST.get('xlabel') == '':
                xlabel = ''
            else:
                xlabel = request.POST.get('xlabel')
            if request.POST.get('ylabel') == '':
                ylabel = ''
            else:
                ylabel = request.POST.get('ylabel')
            if request.POST.get('titlename') == '':
                title_name = ''
            else:
                title_name = request.POST.get('titlename')
            if graph_type == 'bar' or graph_type == 'Bar':
                context['plot'] = df.plot(kind='bar', x=column1, y=column2, figsize=(10, 5))
                context['plot']=plt.title(title_name)
                context['plot']=plt.xlabel(xlabel)
                context['plot']=plt.ylabel(ylabel)
                context['plot'].get_figure().savefig('media/plot.png')
                context['plot_url'] = 'media/plot.png'
            elif graph_type == 'line' or graph_type == 'Line':
                context['plot'] = df.plot(kind='line', x=column1, y=column2, figsize=(10, 5))
                context['plot']=plt.title(title_name)
                context['plot']=plt.xlabel(xlabel)
                context['plot']=plt.ylabel(ylabel)
                context['plot'].get_figure().savefig('media/plot.png')
                context['plot_url'] = 'media/plot.png'
            elif graph_type == 'scatter' or graph_type == 'Scatter':
                context['plot'] = df.plot(kind='scatter', x=column1, y=column2, figsize=(10, 5))
                context['plot']=plt.title(title_name)
                context['plot']=plt.xlabel(xlabel)
                context['plot']=plt.ylabel(ylabel)
                context['plot'].get_figure().savefig('media/plot.png')
                context['plot_url'] = 'media/plot.png'
            elif graph_type == 'hist' or graph_type == 'Hist':
                context['plot'] = df.hist(column1, column2, figsize=(10, 5))
                context['plot'] = df.plot(kind='hist', x=column1, y=column2, figsize=(10, 5))
                context['plot']=plt.title(title_name)
                context['plot']=plt.xlabel(xlabel)
                context['plot']=plt.ylabel(ylabel)
                context['plot'].get_figure().savefig('media/plot.png')
                context['plot_url'] = 'media/plot.png'
        elif uploaded_file.name.endswith('.xls'):
            df = pd.read_excel(uploaded_file)
            context['df'] = df
            context['head'] = df.head(10)
            if request.POST.get('column1') == '' or request.POST.get('column1') not in df.columns:
                column1 = df.columns[0]
            else:
                column1 = request.POST.get('column1')
            if request.POST.get('column2') == '' or request.POST.get('column2') not in df.columns:
                column2 = df.columns[1]
            else:
                column2 = request.POST.get('column2')
            graph_type = request.POST.get('graphtype')
            if request.POST.get('xlabel') == '':
                xlabel = ''
            else:
                xlabel = request.POST.get('xlabel')
            if request.POST.get('ylabel') == '':
                ylabel = ''
            else:
                ylabel = request.POST.get('ylabel')
            if request.POST.get('titlename') == '':
                title_name = ''
            else:
                title_name = request.POST.get('titlename')
            if graph_type == 'bar' or graph_type == 'Bar':
                context['plot'] = df.plot(kind='bar', x=column1, y=column2, figsize=(10, 5))
                context['plot']=plt.title(title_name)
                context['plot']=plt.xlabel(xlabel)
                context['plot']=plt.ylabel(ylabel)
                context['plot'].get_figure().savefig('media/plot.png')
                context['plot_url'] = 'media/plot.png'
            elif graph_type == 'line' or graph_type == 'Line':
                context['plot'] = df.plot(kind='line', x=column1, y=column2, figsize=(10, 5))
                context['plot']=plt.title(title_name)
                context['plot']=plt.xlabel(xlabel)
                context['plot']=plt.ylabel(ylabel)
                context['plot'].get_figure().savefig('media/plot.png')
                context['plot_url'] = 'media/plot.png'
            elif graph_type == 'scatter' or graph_type == 'Scatter':
                context['plot'] = df.plot(kind='scatter', x=column1, y=column2, figsize=(10, 5))
                context['plot']=plt.title(title_name)
                context['plot']=plt.xlabel(xlabel)
                context['plot']=plt.ylabel(ylabel)
                context['plot'].get_figure().savefig('media/plot.png')
                context['plot_url'] = 'media/plot.png'
            elif graph_type == 'hist' or graph_type == 'Hist':
                context['plot'] = df.plot(kind='hist', x=column1, y=column2, figsize=(10, 5))
                context['plot']=plt.title(title_name)
                context['plot']=plt.xlabel(xlabel)
                context['plot']=plt.ylabel(ylabel)
                context['plot'].get_figure().savefig('media/plot.png')
                context['plot_url'] = 'media/plot.png'
        else:
            context['error'] = 'File type not supported'
    return render(request, 'web/home.html',context)




