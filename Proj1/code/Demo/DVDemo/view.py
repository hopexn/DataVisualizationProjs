import os

import pandas as pd
from django.shortcuts import render

from DVDemo.settings import BASE_DIR


def index(request, page_name):
    return render(request, page_name)

def default(request):
    return render(request, "index.html")


def style_differ1(request):
    content = ""
    files = os.listdir(os.path.join(BASE_DIR, "../results/"))
    for file in files:
        if file[-3:] == ".bk":
            filename = file[:-2] + "jpg"
        elif file[-3:] == "jbk":
            filename = file[:-2] + "peg"
        else:
            continue
        
        img_html = "<li class='col-sm-4'><a href='style_differ/{}'><img src='/assets/pics/{}'></a></li>" \
            .format(filename, filename)
        print()
        content += img_html
    
    img_ctxt = {'content': content}
    return render(request, "style_differ.html", img_ctxt)


def style_differ2(request, image_name):
    num_pics_disp = 50
    result_base_path = os.path.join(BASE_DIR, "../results/")
    result_path = result_base_path + image_name[:-3] + "bk"
    
    result = pd.read_csv(result_path)
    result = result.sort_values('diff', ascending=True).head(num_pics_disp).reset_index()
    
    content = ""
    for i in range(1, num_pics_disp):
        filename = result.loc[i, 'filename']
        filename_id = filename[:-3]
        img_html = "<li class='col-sm-4'><img src='/assets/pics/{}'></li>" \
            .format(filename, filename, filename_id)
        print()
        content += img_html
    
    img_ctxt = {'img_name': image_name, 'content': content}
    return render(request, "style_differ2.html", img_ctxt)
