import zipfile

def get_file_from_zip(filename, filename_fz):
    fanstasy_zip = zipfile.ZipFile(filename)  # 解压zip文件
    fanstasy_zip.extract(filename_fz)  # 从zip文件中获得名为filename_fz的文件
    fanstasy_zip.close()  # 关闭zip文件

if __name__ == "__main__":
    get_file_from_zip()