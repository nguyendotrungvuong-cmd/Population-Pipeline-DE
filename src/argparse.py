import argparse


def arg_parse():
    parser = argparse.ArgumentParser(description="Dữ liệu dân số ")
    parser.add_argument("--country", type=str, default="vietnam")
    parser.add_argument("--mode", choices=["api", "load_json"], default="api")
    return parser.parse_args()
