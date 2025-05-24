#!/usr/bin/env python3

import argparse
from interpreter import run_nara_code

def main():
    parser = argparse.ArgumentParser(description="🕉️ NĀRA CLI - Run Sanskrit-based AI agents")
    parser.add_argument("file", help=".nara file to execute")
    args = parser.parse_args()

    with open(args.file, "r", encoding="utf-8") as f:
        code = f.read()
        run_nara_code(code)

if __name__ == "__main__":
    main()
