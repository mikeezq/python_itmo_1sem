import random
import string
import os
from argparse import ArgumentParser
from latex_functions.latex_functions import generate_latex_table, generate_latex_image

def generate_random_table_values():
    chrs = string.ascii_letters + string.digits
    list_to_table = [[''] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            list_to_table[i][j] = ''.join(random.choices(chrs, k=random.randint(1, 10)))

    return list_to_table


def prepare_document_header(latex_path: str):
    with open(latex_path, "w") as file:
        file.write("\\documentclass{article}\n")
        file.write("\\usepackage{graphicx}\n")
        file.write("\\begin{document}\n")


def prepare_document_end(latex_path: str):
    with open(latex_path, "a") as file:
        file.write("\\end{document}\n")


def prepare_latex_document(latex_path: str, image_path: str):
    prepare_document_header(latex_path)

    table_values = generate_random_table_values()
    generate_latex_table(table_values, latex_path)
    generate_latex_image(image_path, latex_path)

    prepare_document_end(latex_path)



def parse_args():
    parser = ArgumentParser()

    script_dir = os.path.dirname(os.path.realpath(__file__))
    parser.add_argument("--latex-path", help='Path where to save latex code',
                        default=os.path.join(script_dir, "artifacts/artifacts.tex"))

    parser.add_argument("--image-path", help='Path for image',
                        default=os.path.join(script_dir, "artifacts/random.png"))


    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    latex_path = args.latex_path
    image_path = args.image_path
    prepare_latex_document(latex_path, image_path)

