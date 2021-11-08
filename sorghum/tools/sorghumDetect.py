import os

import detect
from sorghum.settings import BASE_DIR, STATIC_URL


def convertPath(undetectPath):

    return undetectPath.replace("undetect","detect")

def detect_one_pic(relativePath):
    # if len(relativePath) == 0:
    #     relativePath = "runs/undetect/3_sorghum.jpg"  # 举个栗子
    print("BASE_DIR:" + str(BASE_DIR))
    print("detect_one_pic函数中的STATIC_URL：" + str(STATIC_URL))
    res_dict = detect.run(weights=os.path.join(str(BASE_DIR),"runs/train/sorghum_result/weights/best.pt"),
                          source=os.path.join(str(BASE_DIR) + str(STATIC_URL),relativePath))
    print("result dict：" + str(res_dict))
    res_dict["relativePath"] = convertPath(relativePath)
    return res_dict



def main():
# if __name__ == '__main__':





    relativePath= "runs/undetect/3_sorghum.jpg"
    print(BASE_DIR)
    res_dict = detect.run(weights="../../runs/train/sorghum_result/weights/best.pt",source=os.path.join(str(BASE_DIR) + str(STATIC_URL),relativePath))
    print("result dict：" + str(res_dict))