from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Virtual KITTI"
PROJECT_NAME_FULL: str = "Virtual KITTI Dataset"
HIDE_DATASET = True  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_NC_SA_3_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Automotive()]
CATEGORY: Category = Category.SelfDriving()

CV_TASKS: List[CVTask] = [
    CVTask.InstanceSegmentation(),
    CVTask.SemanticSegmentation(),
    CVTask.ObjectDetection(),
]
ANNOTATION_TYPES: List[AnnotationType] = [
    AnnotationType.InstanceSegmentation(),
    AnnotationType.SemanticSegmentation(),
    AnnotationType.ObjectDetection(),
]

RELEASE_DATE: Optional[str] = "2016-08-10"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = (
    "https://europe.naverlabs.com/research/computer-vision/proxy-virtual-worlds-vkitti-1/"
)
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 12999519
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/virtual-kitti"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
    "vkitti_1.3.1_depthgt.tar": "http://download.europe.naverlabs.com/virtual-kitti-1.3.1/vkitti_1.3.1_depthgt.tar",
    "vkitti_1.3.1_extrinsicsgt.tar.gz": "http://download.europe.naverlabs.com/virtual-kitti-1.3.1/vkitti_1.3.1_extrinsicsgt.tar.gz",
    "vkitti_1.3.1_flowgt.tar": "http://download.europe.naverlabs.com/virtual-kitti-1.3.1/vkitti_1.3.1_flowgt.tar",
    "vkitti_1.3.1_motgt.tar.gz": "http://download.europe.naverlabs.com/virtual-kitti-1.3.1/vkitti_1.3.1_motgt.tar.gz",
    "vkitti_1.3.1_rgb.tar": "http://download.europe.naverlabs.com/virtual-kitti-1.3.1/vkitti_1.3.1_rgb.tar",
    "vkitti_1.3.1_scenegt.tar": "http://download.europe.naverlabs.com/virtual-kitti-1.3.1/vkitti_1.3.1_scenegt.tar",
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "building": [230, 25, 75],
    "car": [60, 180, 75],
    "guard rail": [255, 225, 25],
    "misc": [0, 130, 200],
    "pole": [245, 130, 48],
    "road": [145, 30, 180],
    "sky": [70, 240, 240],
    "terrain": [240, 50, 230],
    "traffic light": [210, 245, 60],
    "traffic sign": [250, 190, 212],
    "tree": [0, 128, 128],
    "truck": [220, 190, 255],
    "van": [170, 110, 40],
    "vegetation": [255, 250, 200],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
# Use dict key to specify name for a button
PAPER: Optional[Union[str, List[str], Dict[str, str]]] = "https://arxiv.org/pdf/1605.06457.pdf"
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = None

CITATION_URL: Optional[str] = None
AUTHORS: Optional[List[str]] = ["Adrien Gaidon", "Qiao Wang", "Yohann Cabon", "Eleonora Vig"]
AUTHORS_CONTACTS: Optional[List[str]] = [
    "adrien.gaidon@xrce.xerox.com",
    "yohann.cabon@xrce.xerox.com",
    " qiao.wang@asu.edu",
    " eleonora.vig@dlr.de",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = ["FR-US joint research group"]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = None

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with string value to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = {
    "__PRETEXT__": "Additionally, images are grouped by ***im id***. Also every image contains information about its ***sequence***, ***subfolder***. Explore it in supervisely labeling tool. Images labels have ***color***, ***model***, ***occluded*** and ***occupancy ratio***"
}
TAGS: Optional[List[str]] = None


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################    0001_15-deg-left_00000 0006_30-deg-left_00140 0006_30-deg-left_00140
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
