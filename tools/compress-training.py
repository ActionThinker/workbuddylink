"""培训现场照片压缩管线：inbox/<场次>/ 原图 → assets/training/<slug>/web/photo-NN.webp

用法: python tools/compress-training.py <inbox文件夹> <slug>
示例: python tools/compress-training.py "inbox/梁溪区培训" "2026-06-wuxi-liangxi"

规则:
- 按 EXIF 拍摄时间排序（无 EXIF 按文件名），输出 photo-01.webp 起
- EXIF 方向纠正 → 等比缩到最长边 1280 → WEBP quality 78
- 每张目标 <250KB（硬上限 1.2MB），超标自动降 quality 重试
"""
import sys
from pathlib import Path

from PIL import Image, ImageOps

MAX_EDGE = 1280
QUALITY = 78
TARGET_BYTES = 250 * 1024
HARD_BYTES = 1_200_000
SUPPORTED = {".jpg", ".jpeg", ".png"}


def shot_time(path: Path) -> int:
    try:
        exif = Image.open(path).getexif()
        return int(exif.get(306, 0) or 0)  # 306 = DateTime
    except Exception:
        return 0


def compress_one(src: Path, dst: Path) -> int:
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im)
        im.thumbnail((MAX_EDGE, MAX_EDGE))
        if im.mode not in ("RGB", "RGBA"):
            im = im.convert("RGB")
        q = QUALITY
        while True:
            im.save(dst, "WEBP", quality=q, method=6)
            size = dst.stat().st_size
            if size <= TARGET_BYTES or q <= 60 or size <= HARD_BYTES:
                return size
            q -= 8


def main() -> None:
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    src_dir = Path(sys.argv[1])
    slug = sys.argv[2]
    if not src_dir.is_dir():
        print(f"文件夹不存在: {src_dir}")
        sys.exit(1)
    photos = sorted(
        [p for p in src_dir.iterdir() if p.suffix.lower() in SUPPORTED],
        key=lambda p: (shot_time(p), p.name),
    )
    if not photos:
        print(f"未找到 JPG/PNG 图片: {src_dir}")
        sys.exit(1)
    out_dir = Path("assets/training") / slug / "web"
    out_dir.mkdir(parents=True, exist_ok=True)
    for i, src in enumerate(photos, 1):
        dst = out_dir / f"photo-{i:02d}.webp"
        size = compress_one(src, dst)
        print(f"{dst}  {size // 1024}KB")
    print(f"完成: {len(photos)} 张 → {out_dir}")


if __name__ == "__main__":
    main()
