import os

LINE_CHANNEL_ACCESS_TOKEN = os.environ.get('LINE_CHANNEL_ACCESS_TOKEN')
LINE_CHANNEL_SECRET = os.environ.get('LINE_CHANNEL_SECRET')

ARXIV_CATEGORIES = ["cs.CV"] # ["cs.*"]
KEYWORD_SCORES = {
    "nerf": 4,
    
}
SCORE_THRESHOLD = 3

# KEYWORD_SCORES = {
#     "3d object detetection": 3,
#     "visual odometry": 3,
#     "nerf": 3,
#     "neural radiance fields": 3,
#     "Fusion": 2,
#     "LiDAR": 1,
#     "Camera": 1,
#     "object Detection": 1,
#     "semantic segmentation": 1,
#     "feature matching": 1,
#     "3D": 1,
#     "Domain Adaptation": 1,
#     "semi-supervised": 1,
#     "unsupervised": 1,
    
# }