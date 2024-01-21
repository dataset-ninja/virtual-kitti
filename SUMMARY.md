**Virtual KITTI Dataset** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the automotive industry. 

The dataset consists of 63730 images with 3314922 labeled objects belonging to 14 different classes including *road*, *sky*, *terrain*, and other: *tree*, *car*, *traffic sign*, *building*, *pole*, *van*, *guard rail*, *vegetation*, *traffic light*, *misc*, and *truck*.

Images in the Virtual KITTI dataset have pixel-level instance segmentation annotations. All images are labeled (i.e. with annotations). There are no pre-defined <i>train/val/test</i> splits in the dataset. Additionally, images are grouped by ***im id***. Also every image contains information about its ***sequence***, ***subfolder***. Explore it in supervisely labeling tool. Images labels have ***color***, ***model***, ***occluded*** and ***occupancy ratio***. The dataset was released in 2016 by the FR-US joint research group.

Here are the visualized examples for the classes:

[Dataset classes](https://github.com/dataset-ninja/virtual-kitti/raw/main/visualizations/classes_preview.webm)
