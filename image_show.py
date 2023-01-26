import os
import matplotlib.pyplot as plt
import matplotlib.image as img
from tqdm import tqdm

DATA1_ROOT = "/Users/cillian/Documents/Github/image_concat/Ground Truth"  # Ground Truth
DATA2_ROOT = "/Users/cillian/Documents/Github/image_concat/Vanilla Faster R-CNN"  # Vanilla Faster R-CNN
DATA3_ROOT = "/Users/cillian/Documents/Github/image_concat/Co-mining"  # Co-mining
DATA4_ROOT = "/Users/cillian/Documents/Github/image_concat/Ours"  # Ours


folder_list = [DATA1_ROOT, DATA2_ROOT, DATA3_ROOT, DATA4_ROOT]


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print(f"Error: Creating directory. {directory}")


def show_image(image_name, image_dir_list, save_dir, n_rows=2, n_cols=2):
    n_rows = n_rows
    n_cols = n_cols
    fig, axes = plt.subplots(n_rows, n_cols)

    idx = 0
    for row_num in range(n_rows):
        for col_num in range(n_cols):
            image_dir = image_dir_list[idx]
            dir_name = os.path.basename(image_dir)
            image_path = os.path.join(image_dir, image_name)
            image = img.imread(image_path)
            idx += 1

            ax = axes[row_num][col_num]
            # ax.imshow(image, aspect="auto")
            ax.imshow(image)
            ax.axes.xaxis.set_visible(False)
            ax.axes.yaxis.set_visible(False)
            ax.set_title(f"{dir_name}")

    fig.suptitle(f"{image_name}")
    fig.tight_layout()

    create_folder(save_dir)
    save_image_path = os.path.join(save_dir, f"{image_name}")
    plt.savefig(save_image_path, dpi=400)
    # plt.show()


if __name__ == "__main__":
    image_name_list = os.listdir(DATA1_ROOT)
    for image_name in tqdm(image_name_list):
        show_image(image_name, folder_list, "result_images")
