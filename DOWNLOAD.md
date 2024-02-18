Dataset **Virtual KITTI** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://www.dropbox.com/scl/fi/5393pa1re7879ji80gdi2/virtual-kitti-DatasetNinja.tar?rlkey=o1k7okxdf5u8w54ov6nx83dp2&dl=1)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Virtual KITTI', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [vkitti_1.3.1_depthgt.tar](https://download.europe.naverlabs.com/virtual-kitti-1.3.1/vkitti_1.3.1_depthgt.tar)
- [vkitti_1.3.1_extrinsicsgt.tar.gz](https://download.europe.naverlabs.com/virtual-kitti-1.3.1/vkitti_1.3.1_extrinsicsgt.tar.gz)
- [vkitti_1.3.1_flowgt.tar](https://download.europe.naverlabs.com/virtual-kitti-1.3.1/vkitti_1.3.1_flowgt.tar)
- [vkitti_1.3.1_motgt.tar.gz](https://download.europe.naverlabs.com/virtual-kitti-1.3.1/vkitti_1.3.1_motgt.tar.gz)
- [vkitti_1.3.1_rgb.tar](https://download.europe.naverlabs.com/virtual-kitti-1.3.1/vkitti_1.3.1_rgb.tar)
- [vkitti_1.3.1_scenegt.tar](https://download.europe.naverlabs.com/virtual-kitti-1.3.1/vkitti_1.3.1_scenegt.tar)
