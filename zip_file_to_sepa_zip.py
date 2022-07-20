import os
import zipfile
from tqdm import tqdm

def zipDir(dirpath, outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, '')
        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()


if __name__ == "__main__":
    root_path = '/data/gongjunhao/kinetics-dataset/frames/train'
    save_path = '/data/gongjunhao/kinetics-dataset/frames/tar'
    for file in tqdm(os.listdir(root_path)):
        input_path = os.path.join(root_path, file)
        output_path = os.path.join(save_path, file.replace(' ', '_')+'.zip')
        zipDir(input_path, output_path)
