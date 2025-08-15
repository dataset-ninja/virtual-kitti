Dataset **Virtual KITTI** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMzM5MF9WaXJ0dWFsIEtJVFRJL3ZpcnR1YWwta2l0dGktRGF0YXNldE5pbmphLnRhciIsICJzaWciOiAiNGs4bklHZzhhdm5VVWxCMXJKL3BnOCsxbjFQVHR4UEJCY282ekwwdjdwaz0ifQ==?response-content-disposition=attachment%3B%20filename%3D%22virtual-kitti-DatasetNinja.tar%22)

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
