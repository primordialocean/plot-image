import matplotlib.pyplot as plt
import matplotlib_scalebar.scalebar as scale
from adjustText import adjust_text
import numpy as np
import pandas as pd

# スポット分析の描画
def plot_point(ax, x, y, points, crystals):
    ax.plot(x, y, "o", mec="w", c="r")
    # adjust_text()に渡すためにリストに格納する
    texts = [
        plt.text(
            x[i], y[i],
            crystals[i]+"("+str(int(points[i]))+")",
            ha="center", va="center", c="r"
            )
        for i in range(len(x))
    ]
    # adjust_text()に渡すことで位置をよしなに調整してくれる
    adjust_text(
        texts,
        # 矢印入れた方がいいときはコメントを外す
        # arrowprops=dict(arrowstyle='->', color='red')
        )

# スケールバーの計算
def calc_scale(df, img):
    # 倍率を取得
    magnifications = df["Magnification"].values.tolist()
    magnification = magnifications[0]
    # スケールバーの引数を計算する
    img_tuple = np.array(img).shape
    row = img_tuple[1]
    # 電子顕微鏡の画面サイズは横12cmを基準としているため
    # なぜか12.5cmで正確な値になる．倍率計算に用いている領域と実際に表示される領域が異なるため？
    real_width = 0.125 / magnification
    meter_per_pixel = real_width / row
    return meter_per_pixel

def main():
    sample = "input"
    df = pd.read_excel("input.xlsx", sheet_name="opx")
    df = df[ df["Sample"] == sample ]
    filenames = df["Filename"].values.tolist()
    list_filenames = list(set(filenames))
    for filename in list_filenames:
        df_filter = df[ df["Filename"] == filename ].reset_index(drop=True)
        
        x_coord = df_filter["X"].values.tolist()
        y_coord = df_filter["Y"].values.tolist()
        crystals = df_filter["Crystal"].values.tolist()
        points = df_filter["Mg#"].values.tolist()
        
        pic_name = filename.replace(".tif", "")
        img = plt.imread("img_"+sample+"//"+filename)
        fig, ax = plt.subplots()
        # 画像を表示
        ax.imshow(img, cmap = "gray")
        plot_point(ax, x_coord, y_coord, points, crystals)
        # matplotlibの目盛を非表示
        ax.set_axis_off()
        # 試料名を入力
        ax.text(
            0.01, 0.99, sample,
            ha="left", va="top", c="w", fontsize=14, transform=ax.transAxes
            )
        # スケールバーを描画
        meter_per_pixel = calc_scale(df_filter, img)
        scalebar = scale.ScaleBar(
            meter_per_pixel,
            units="m", location="lower right", scale_loc="top",
            length_fraction=0.250
            ) # 1 pixel = 0.2 meter
        plt.gca().add_artist(scalebar)
        # 画像を保存
        plt.savefig(
            "img_output\\"+pic_name+".jpg",
            dpi=600, bbox_inches='tight', pad_inches=0
            )
        # メモリを解放
        plt.clf()
        plt.close()

if __name__ == "__main__":
    main()
