import os
import shutil
from collections import defaultdict
from urllib.parse import unquote, urlparse

import numpy as np
import supervisely as sly
from cv2 import connectedComponents
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import (
    dir_exists,
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
)
from tqdm import tqdm

import src.settings as s


def download_dataset(teamfiles_dir: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
        parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name_with_ext = unquote(file_name_with_ext)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        local_path = os.path.join(storage_dir, file_name_with_ext)
        teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

        fsize = api.file.get_directory_size(team_id, teamfiles_dir)
        with tqdm(
            desc=f"Downloading '{file_name_with_ext}' to buffer...",
            total=fsize,
            unit="B",
            unit_scale=True,
        ) as pbar:
            api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)
        dataset_path = unpack_if_archive(local_path)

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
        for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
            local_path = os.path.join(storage_dir, file_name_with_ext)
            teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

            if not os.path.exists(get_file_name(local_path)):
                fsize = api.file.get_directory_size(team_id, teamfiles_dir)
                with tqdm(
                    desc=f"Downloading '{file_name_with_ext}' to buffer...",
                    total=fsize,
                    unit="B",
                    unit_scale=True,
                ) as pbar:
                    api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)

                sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
                unpack_if_archive(local_path)
            else:
                sly.logger.info(
                    f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
                )

        dataset_path = storage_dir
    return dataset_path


def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    ### Function should read local dataset and upload it to Supervisely project, then return project info.###
    raise NotImplementedError("The converter should be implemented manually.")
    images_path = "/home/alex/DATASETS/TODO/Virtual KITTI/vkitti_1.3.1_rgb"
    flow_path = "/home/alex/DATASETS/TODO/Virtual KITTI/vkitti_1.3.1_flowgt"
    depth_path = "/home/alex/DATASETS/TODO/Virtual KITTI/vkitti_1.3.1_depthgt"
    masks_path = "/home/alex/DATASETS/TODO/Virtual KITTI/vkitti_1.3.1_scenegt"
    bboxes_path = "/home/alex/DATASETS/TODO/Virtual KITTI/vkitti_1.3.1_motgt"

    batch_size = 30
    ds_name = "ds"
    group_tag_name = "im_id"
    masks_suffix = "_scenegt_rgb_encoding.txt"

    def get_unique_colors(img):
        unique_colors = []
        img = img.astype(np.int32)
        h, w = img.shape[:2]
        colhash = img[:, :, 0] * 256 * 256 + img[:, :, 1] * 256 + img[:, :, 2]
        unq, unq_inv, unq_cnt = np.unique(colhash, return_inverse=True, return_counts=True)
        indxs = np.split(np.argsort(unq_inv), np.cumsum(unq_cnt[:-1]))
        col2indx = {unq[i]: indxs[i][0] for i in range(len(unq))}
        for col, indx in col2indx.items():
            if col != 0:
                unique_colors.append((col // (256**2), (col // 256) % 256, col % 256))

        return unique_colors

    def create_ann(image_path):
        labels = []

        id_data = sequence + "_" + subfolder + "_" + get_file_name(image_path)
        group_id = sly.Tag(tag_id, value=id_data)

        img_height = 375
        img_wight = 1242

        subfolder_value = image_path.split("/")[-2]
        subfolder_tag = sly.Tag(subfolder_meta, value=subfolder_value)
        sequence_tag = sly.Tag(sequence_meta, value=sequence)

        image_name = get_file_name_with_ext(image_path)

        mask_path = os.path.join(curr_masks_path, image_name)
        if file_exists(mask_path):
            mask_np = sly.imaging.image.read(mask_path)
            unique_colors = get_unique_colors(mask_np)
            for color in unique_colors:
                class_name = color_to_class_name[color]
                obj_class = name_to_class[class_name]
                mask = np.all(mask_np == color, axis=2)
                ret, curr_mask = connectedComponents(mask.astype("uint8"), connectivity=8)
                for i in range(1, ret):
                    obj_mask = curr_mask == i
                    bitmap = sly.Bitmap(data=obj_mask)
                    if bitmap.area > 50:
                        label = sly.Label(bitmap, obj_class)
                        labels.append(label)

        bbox_data = frame_to_data.get(get_file_name(image_path))
        if bbox_data is not None:
            for curr_bbox_data in bbox_data:
                obj_class = name_to_class[curr_bbox_data[0]]
                model_value = curr_bbox_data[1]
                model = sly.Tag(model_meta, value=model_value)
                color_value = curr_bbox_data[2]
                color_tag = sly.Tag(color_meta, value=color_value)
                occupancy_value = curr_bbox_data[3]
                occupancy = sly.Tag(occupancy_meta, value=occupancy_value)
                occluded_value = idx_to_occluded[curr_bbox_data[4]]
                occluded = sly.Tag(occluded_meta, value=occluded_value)
                coords = curr_bbox_data[-1]

                left = coords[0]
                right = coords[2]
                top = coords[1]
                bottom = coords[3]
                rectangle = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
                label = sly.Label(
                    rectangle, obj_class, tags=[model, color_tag, occupancy, occluded]
                )
                labels.append(label)

        return sly.Annotation(
            img_size=(img_height, img_wight),
            labels=labels,
            img_tags=[subfolder_tag, sequence_tag, group_id],
        )

    building = sly.ObjClass("building", sly.AnyGeometry)
    car = sly.ObjClass("car", sly.AnyGeometry)
    guardrail = sly.ObjClass("guard rail", sly.AnyGeometry)
    misc = sly.ObjClass("misc", sly.AnyGeometry)
    pole = sly.ObjClass("pole", sly.AnyGeometry)
    road = sly.ObjClass("road", sly.AnyGeometry)
    sky = sly.ObjClass("sky", sly.AnyGeometry)
    terrain = sly.ObjClass("terrain", sly.AnyGeometry)
    traffic_light = sly.ObjClass("traffic light", sly.AnyGeometry)
    traffic_sign = sly.ObjClass("traffic sign", sly.AnyGeometry)
    tree = sly.ObjClass("tree", sly.AnyGeometry)
    truck = sly.ObjClass("truck", sly.AnyGeometry)
    van = sly.ObjClass("van", sly.AnyGeometry)
    vegetation = sly.ObjClass("vegetation", sly.AnyGeometry)
    # dont_care = sly.ObjClass("dont care", sly.AnyGeometry)

    name_to_class = {
        "Building": building,
        "Car": car,
        "GuardRail": guardrail,
        "Misc": misc,
        "Pole": pole,
        "Road": road,
        "Sky": sky,
        "Terrain": terrain,
        "TrafficLight": traffic_light,
        "TrafficSign": traffic_sign,
        "Tree": tree,
        "Truck": truck,
        "Van": van,
        "Vegetation": vegetation,
        # "DontCare": dont_care,
    }

    subfolder_meta = sly.TagMeta("subfolder", sly.TagValueType.ANY_STRING)
    tag_id = sly.TagMeta(group_tag_name, sly.TagValueType.ANY_STRING)

    model_meta = sly.TagMeta("model", sly.TagValueType.ANY_STRING)
    color_meta = sly.TagMeta("color", sly.TagValueType.ANY_STRING)
    occupancy_meta = sly.TagMeta("occupancy ratio", sly.TagValueType.ANY_NUMBER)
    occluded_meta = sly.TagMeta("occluded", sly.TagValueType.ANY_STRING)
    sequence_meta = sly.TagMeta("sequence", sly.TagValueType.ANY_STRING)

    idx_to_occluded = {0: "not occluded", 1: "occluded", 2: "heavily occluded"}

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(
        obj_classes=list(name_to_class.values()),
        tag_metas=[
            subfolder_meta,
            tag_id,
            model_meta,
            color_meta,
            occupancy_meta,
            occluded_meta,
            sequence_meta,
        ],
    )
    api.project.update_meta(project.id, meta.to_json())
    api.project.images_grouping(id=project.id, enable=True, tag_name=group_tag_name)

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    for data_path in [images_path, flow_path, depth_path]:
        prefix = data_path.split("_")[-1] + "_"
        for sequence in os.listdir(data_path):
            curr_sequence_path = os.path.join(data_path, sequence)

            if dir_exists(curr_sequence_path):
                for subfolder in os.listdir(curr_sequence_path):
                    curr_images_path = os.path.join(curr_sequence_path, subfolder)
                    curr_masks_path = os.path.join(masks_path, sequence, subfolder)
                    category_to_color_name = sequence + "_" + subfolder + masks_suffix
                    category_to_color_path = os.path.join(masks_path, category_to_color_name)
                    color_to_class_name = {}
                    with open(category_to_color_path) as f:
                        content = f.read().split("\n")
                        for idx, curr_data in enumerate(content):
                            if idx == 0 or len(curr_data) == 0:
                                continue
                            list_data = curr_data.split(" ")
                            color_to_class_name[
                                (int(list_data[1]), int(list_data[2]), int(list_data[3]))
                            ] = list_data[0].split(":")[0]

                    curr_bboxes_name = sequence + "_" + subfolder + ".txt"
                    curr_bboxes_path = os.path.join(bboxes_path, curr_bboxes_name)
                    frame_to_data = defaultdict(list)
                    with open(curr_bboxes_path) as f:
                        content = f.read().split("\n")
                        for idx, curr_data in enumerate(content):
                            if idx == 0 or len(curr_data) == 0:
                                continue
                            list_data = curr_data.split(" ")
                            frame_to_data[list_data[0].zfill(5)].append(
                                [
                                    list_data[-4],
                                    list_data[-2],
                                    list_data[-1],
                                    float(list_data[-5]),
                                    int(list_data[4]),
                                    list(map(int, list_data[6:10])),
                                ]
                            )

                    images_names = os.listdir(curr_images_path)

                    progress = sly.Progress(
                        "Create sequence {}, folder {}".format(sequence, subfolder),
                        len(images_names),
                    )

                    for images_names_batch in sly.batched(images_names, batch_size=batch_size):
                        img_pathes_batch = [
                            os.path.join(curr_images_path, image_name)
                            for image_name in images_names_batch
                        ]

                        unique_images_names = [
                            prefix + sequence + "_" + subfolder + "_" + im_name
                            for im_name in images_names_batch
                        ]

                        img_infos = api.image.upload_paths(
                            dataset.id, unique_images_names, img_pathes_batch
                        )
                        img_ids = [im_info.id for im_info in img_infos]

                        anns = [create_ann(image_path) for image_path in img_pathes_batch]
                        api.annotation.upload_anns(img_ids, anns)

                        progress.iters_done_report(len(images_names_batch))

    return project
