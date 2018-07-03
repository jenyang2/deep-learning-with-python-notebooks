import os

# 핸즈온 번역서 노트북을 위한 유틸리티 함수들입니다.

def save_fig(fig_id):
    """출판을 위한 고해상 이미지를 만듭니다"""
    path = os.path.join("./images/", fig_id + ".png")
    plt.tight_layout()
    plt.savefig(path, format="png", dpi=300)
