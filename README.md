## 美展图像相似度检测

- 运行方法
1. 将美展图片复制到imgs和Demo/templates/assets/pics下, excel文件改名为data.xls（文件太大不便上传）
2. 运行FeatureExtraction.ipynb, 运行结果会保存在results文件夹下
3. 进入Demo文件夹, 运行`python ./manage.py runserver 0.0.0.0:8000`启动demo
4. 浏览器访问http://localhost:8000

文件目录结构:
$ tree -L 1 .
.
├── data.xls
├── Demo
├── FeatureExtraction.ipynb
├── imgs
└── results
