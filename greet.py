#!/usr/bin/env python3
"""一个最小的问候脚本。用来验证仓库能跑，没别的野心。"""

import sys


def greet(name: str = "") -> str:
    who = name.strip() or "你"
    return f"你好，{who}。\n今天也慢慢来。"


def main() -> int:
    print(greet(" ".join(sys.argv[1:])))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
