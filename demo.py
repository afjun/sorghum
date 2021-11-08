import detect
if __name__ == '__main__':
    res_dict = detect.run(weights="./runs/train/sorghum_result/weights/best.pt",source="./data/images/sorghum/3_sorghum.jpg")
    print("result dict：" + str(res_dict))