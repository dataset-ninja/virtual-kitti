Dataset **Virtual KITTI** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzMzOTBfVmlydHVhbCBLSVRUSS92aXJ0dWFsLWtpdHRpLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogIkw3cnYyQ2hHcWo3MHYzZmxpTHRHc2VIeWpFeUlraUQwZis3WUtCOHlmZU09In0=)

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

- [vkitti_1.3.1_depthgt.tar](http://download.europe.naverlabs.com/virtual-kitti-1.3.1/vkitti_1.3.1_depthgt.tar)
- [vkitti_1.3.1_extrinsicsgt.tar.gz](http://download.europe.naverlabs.com/virtual-kitti-1.3.1/vkitti_1.3.1_extrinsicsgt.tar.gz)
- [vkitti_1.3.1_flowgt.tar](http://download.europe.naverlabs.com/virtual-kitti-1.3.1/vkitti_1.3.1_flowgt.tar)
- [vkitti_1.3.1_motgt.tar.gz](http://download.europe.naverlabs.com/virtual-kitti-1.3.1/vkitti_1.3.1_motgt.tar.gz)
- [vkitti_1.3.1_rgb.tar](http://download.europe.naverlabs.com/virtual-kitti-1.3.1/vkitti_1.3.1_rgb.tar)
- [vkitti_1.3.1_scenegt.tar](http://download.europe.naverlabs.com/virtual-kitti-1.3.1/vkitti_1.3.1_scenegt.tar)
